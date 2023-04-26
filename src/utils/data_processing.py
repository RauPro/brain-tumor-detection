import os
import shutil
import imutils
from matplotlib import pyplot as plt
import cv2
from tensorflow import keras

def count_instances(directory):
    """Count the number of instances in a directory.

    Parameters
    ----------
    directory : str
        Path to the directory.

    Returns
    -------
    int
        Number of instances in the directory.

    """
    return len(os.listdir(directory))


def copy_instances(source_directory, target_directory):
    """Copy the instances from a source directory to a target directory.

    Parameters
    ----------
    source_directory : str
        Path to the source directory.
    target_directory : str
        Path to the target directory.

    """
    for instance in os.listdir(source_directory):
        shutil.copy(os.path.join(source_directory, instance),
                    os.path.join(target_directory, instance))


def rename_instances(directory, appended_string):
    """Rename the instances in a directory.

    Parameters
    ----------
    directory : str
        Path to the directory.
    appended_string : str
        String to append to the instance name.

    """
    for instance in os.listdir(directory):
        os.rename(os.path.join(directory, instance),
                  os.path.join(directory, appended_string + instance))


# Validate if the directory exists
def validate_directory(directory):
    """Validate if a directory exists.

    Parameters
    ----------
    directory : str
        Path to the directory.

    Returns
    -------
    bool
        True if the directory exists, False otherwise.

    """
    return os.path.isdir(directory)

# Method for data augmented dataset
def make_data_augmented_dataset(file_dir, n_generated_samples, save_to_dir, save_prefix):
    """Make a data augmented dataset.

    Parameters
    ----------
    file_dir : str
        Path to the directory containing the original dataset.
    n_generated_samples : int
        Number of samples to be generated for each image.
    save_to_dir : str
        Path to the directory where the augmented dataset will be saved.
    save_prefix : str
        Prefix of the directory to save samples generated.

    Returns
    -------
    str
        Message indicating if the dataset was successfully created or not.

    """

    if not validate_directory(save_to_dir):
        os.mkdir(save_to_dir)

    if not validate_directory(os.path.join(save_to_dir, save_prefix)):
        os.mkdir(os.path.join(save_to_dir, save_prefix))
    else:
        shutil.rmtree(os.path.join(save_to_dir, save_prefix))
    save_to_dir += save_prefix
    data_gen = keras.preprocessing.image.ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.15,
        zoom_range=0.1,
        brightness_range=[0.2, 1.0],
        horizontal_flip=True,
        vertical_flip=False,
        fill_mode='nearest')

    for file_name in os.listdir(file_dir):
        img = cv2.imread(os.path.join(file_dir, file_name))
        img = img.reshape((1,) + img.shape)
        save_prefix = 'aug_' + file_name[:-4]
        amount = 0
        for _ in data_gen.flow(img, batch_size=1,
                               save_to_dir=save_to_dir,
                               save_prefix=save_prefix,
                               save_format='jpeg'):
            amount += 1
            if amount > n_generated_samples:
                break

    return 'Success in making the data augmented dataset.'

def data_summary(data_path):
    """Summarize the data in a directory.

    Parameters
    ----------
    data_path : str
        Path to the directory containing the data.

    Returns
    -------
    str
        Summary of the data in the directory.
    """
    yes_path = os.path.join(data_path, 'yes')
    no_path = os.path.join(data_path, 'no')
    len_yes = count_instances(yes_path)
    len_no = count_instances(no_path)
    total_len = len_yes + len_no
    percentage_yes = round(len_yes / total_len * 100, 2)
    percentage_no = round(len_no / total_len * 100, 2)
    return 'Total instances: {}\nPercentage of yes: {}%\nPercentage of no: {}%'.format(total_len, percentage_yes, percentage_no)

def crop_brain_contour(image, plot=False):
    """Crop the brain contour of an image.

    Parameters
    ----------
    image : numpy.ndarray
        Image to be cropped.
    plot : bool, optional
        Whether to plot the image or not.

    Returns
    -------
    numpy.ndarray
        Cropped image.

    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold the image, then perform a series of erosions dilations to remove any small regions of noise
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours in thresholded image, then grab the largest one
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cnts.imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)

    # Find the extreme points
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])

    new_image = image[extTop[1]:extBot[1], extLeft[0]:extRight[0]]

    if plot:
        plt.figure()
        plt.subplot(1, 2, 1)
        plt.imshow(image)
        plt.tick_params(axis='both', which='both', bottom=False, top=False,
                        labelbottom=False, right=False, left=False, labelleft=False)
        plt.title('Original Image')

        plt.subplot(1, 2, 2)
        plt.imshow(new_image)

        plt.tick_params(axis='both', which='both', bottom=False, top=False,
                        labelbottom=False, right=False, left=False, labelleft=False)
        plt.title('Cropped Image')

        plt.show()

    return new_image
