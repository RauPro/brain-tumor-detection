import os
import shutil


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
