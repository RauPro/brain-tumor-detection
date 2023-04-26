import os
import shutil

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