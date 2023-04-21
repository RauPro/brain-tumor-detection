# -*- coding: utf-8 -*-
import os

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src.utils.data_processing import validate_directory, copy_instances, rename_instances
import tensorflow as tf
from random import shuffle
import shutil

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
@click.argument('train_ratio', type=float)
@click.argument('validation_ratio', type=float)
def main(input_filepath, output_filepath, train_ratio, validation_ratio):
    """ Runs data processing scripts to turn raw data from (../interim) into
        cleaned data ready to be analyzed (saved in ../interim/split).
        Test ratio = 1 - train_ratio - validation_ratio

        Parameters
        ----------
        input_filepath : str
            Path to the source directory.
        output_filepath : str
            Path to the target directory.
        train_ratio : float
            Ratio of the training set.
        validation_ratio : float
            Ratio of the validation set.
    """
    for class_name in ["yes", "no"]:
        # Create output directory if not exist
        if not validate_directory(output_filepath):
            os.mkdir(output_filepath)
        elif (validate_directory(os.path.join(output_filepath, "train", class_name)) > 0) or \
                (validate_directory(os.path.join(output_filepath, "validate", class_name)) > 0) or \
                (validate_directory(os.path.join(output_filepath, "test", class_name)) > 0) and (
                (len(os.listdir(os.path.join(output_filepath, "train", class_name))) > 0) or (
                len(os.listdir(os.path.join(output_filepath, "validate", class_name))) > 0) or len(
                os.listdir(os.path.join(output_filepath, "test", class_name))) > 0):
            return "The output directory already exists and is not empty. Please delete the directory and try again."

        # Validate if train, validation and test directories exist if not create them
        os.makedirs(os.path.join(output_filepath, "train", class_name), exist_ok=True)
        os.makedirs(os.path.join(output_filepath, "validation", class_name), exist_ok=True)
        os.makedirs(os.path.join(output_filepath, "test", class_name), exist_ok=True)

        #

        # List and shuffle images
        img_files = os.listdir(os.path.join(input_filepath, class_name))
        shuffle(img_files)

        # Calculate the index to split the data
        total_index = len(img_files)
        train_index = int(total_index * train_ratio)
        validation_index = train_index + int(total_index * validation_ratio)

        # Split the data
        train_files = img_files[:train_index]
        validation_files = img_files[train_index:validation_index]
        test_files = img_files[validation_index:]

        # Copy the images to the corresponding directories
        for file in train_files:
            shutil.copy(os.path.join(input_filepath, class_name, file),
                        os.path.join(output_filepath, 'train', class_name, file))
        for file in validation_files:
            shutil.copy(os.path.join(input_filepath, class_name, file),
                        os.path.join(output_filepath, 'validation', class_name, file))
        for file in test_files:
            shutil.copy(os.path.join(input_filepath, class_name, file),
                        os.path.join(output_filepath, 'test', class_name, file))

    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    return 'Success in making the dataset.'


def make_renamed_dataset(input_filepath, target_filepath, appended_string):
    """Copy the instances from a source directory to a target directory.

    Parameters
    ----------
    input_filepath : str
        Path to the source directory.
    target_filepath : str
        Path to the target directory.
    appended_string : str
        String to append to the instance name.

    """
    if not validate_directory(target_filepath):
        os.mkdir(target_filepath)
        copy_instances(input_filepath, target_filepath)
        rename_instances(target_filepath, appended_string)
        return f"Success in making the {appended_string} renamed dataset."
    else:
        raise ValueError('The input target directory is already done.')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
