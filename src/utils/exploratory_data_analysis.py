import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

def plot_sample_images(X, y, n=50):
    """Plot sample images from a dataset.

    Parameters
    ----------
    X : numpy.ndarray
        Array of instances.
    y : numpy.ndarray
        Array of labels.
    n : int
        Number of images to plot.
    ----------

    :return: Plot of sample images.
    """
    for label in [0,1]:
        images = X[np.argwhere(y == label)]
        n_images = images[:n]

        columns_n = 10
        rows_n = int(n/ columns_n)

        plt.figure(figsize=(20, 10))

        i = 1
        for image in n_images:
            plt.subplot(rows_n, columns_n, i)
            plt.imshow(image[0])

            plt.tick_params(axis='both', which='both',
                            top=False, bottom=False, left=False, right=False,
                            labelbottom=False, labeltop=False, labelleft=False,
                            labelright=False)

            i += 1

        label_to_str = lambda label: "Yes" if label == 1 else "No"
        plt.suptitle(f"Brain Tumor: {label_to_str(label)}")
        plt.show()

def load_data(load_dir_list, image_size):
    """Load data from a directory.

    Parameters
    ----------
    load_dir_list : list
        List of directories to load data from.
    image_size : tuple
        Size of the images.

    Returns
    -------
    tuple
        Tuple containing the loaded data.
    """
    X = []
    y = []

    for load_dir in load_dir_list:
        for filename in os.listdir(load_dir):
            image = cv2.imread(os.path.join(load_dir, filename))
            image = cv2.resize(image, image_size)

            X.append(image)
            y.append(1 if load_dir.split('\\')[-1] == 'yes' else 0)

    X = np.array(X)
    y = np.array(y)

    return X, y