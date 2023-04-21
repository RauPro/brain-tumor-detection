# -*- coding: utf-8 -*-
import os

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src.utils.data_processing import validate_directory, copy_instances, rename_instances


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../interim) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


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
