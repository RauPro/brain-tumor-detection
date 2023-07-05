# BrainTumorFinder

## About the BrainTumorFinder Model

BrainTumorFinder is a machine learning model used for the detection of brain tumors. This application leverages TensorFlow and utilizes the VGG19 architecture, along with transfer learning techniques for effective tumor detection. The model has been developed and fine-tuned through three stages: a frozen model, a tuned model, and a fine-tuned model. The original version of the model achieved an accuracy of 98%, whereas the version mapped and split into multiple files managed an accuracy of 90%.

Paper reference: 
[Brain Tumor Detection Using Machine Learning and Deep Learning: A Review](https://webofscience.uca.elogim.com/wos/woscc/full-record/WOS:000848445600003)
[MRI-based brain tumor detection using convolutional deep learning methods and chosen machine learning techniques](https://webofscience.uca.elogim.com/wos/woscc/full-record/WOS:000917653900002)

## Model Dataset

The dataset used in this project comes from Kaggle and consists of 253 images: 98 of them do not have brain tumors, while the rest do. The use of this particular dataset has allowed the model to effectively learn and differentiate between brains with and without tumors.
[Kaggle Dataset](https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection)

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

## Python and Modules Version

For this project, Python 3.8 is recommended. Below is the list of necessary modules and specific versions used in this project:
See requeriments.txt

Please make sure to install these modules in your work environment before attempting to run the model.

## Contributing to the BrainTumorFinder Model

As an open-source project, we welcome and encourage contributions to BrainTumorFinder. If you wish to contribute, there are several ways to do so.

### Reporting Issues

If you come across an error or an issue, please create a new issue on the project's GitHub page. Ensure you describe the problem you have encountered in as much detail as possible, including steps to reproduce it, any error messages received, and the version of the code you are using.

### Pull Requests

If you wish to contribute improvements to the code, please submit a pull request. Ensure you explain in detail what changes you have made and why you believe these are beneficial to the project. Also, make sure that your code adheres to the project's coding and style conventions.

Remember, your contribution can make a significant difference and helps to improve the detection and treatment of brain tumors. Thank you for your collaboration!

## Collaborating with the BrainTumorFinder Model

As an open-source project, we appreciate and encourage contributions to BrainTumorFinder. The project workflow is based on Development (Dev), Quality Assurance (QA), and Production (Main) branches for the Frontend, Backend, and Machine Learning (ML) model. Here's a list of numbered steps on how you can contribute to the project:

1. **Understand the project**: Before you can effectively contribute, it's crucial to understand how the project works, what it does, and how its code is organized.

2. **Identify an issue or improvement**: Once you thoroughly understand the project, you can start looking for ways to improve it.

3. **Create an issue**: If you've found a problem or have an idea for an improvement, the first step is to create an issue on GitHub.

4. **Fork the repository**: To make changes to the code, you need your own copy of the GitHub repository. Fork the repository to create a copy in your GitHub account.

5. **Clone the repository**: Once you have your own fork, you can clone the repository to your local machine.

6. **Create your working branch**: Based on the development branch corresponding to your task (Frontend, Backend, ML), you should create a new branch following the nomenclature:

    - `feature/ml-number`: for new features or improvements in the project.
    - `bugfix/bug-number`: to fix errors in the project.
    - `hotfix/bug-number`:

to address critical issues that arise in production and require a quick solution.
    - `release/version`: to prepare new project versions that will go into production.

7. **Make your changes**: Make the changes you deem appropriate in your local copy of the code.

8. **Commit and push your changes**: When you're satisfied with your changes, commit them to your repository and then push to your fork on GitHub.

9. **Submit a pull request (PR)**: With your changes already on GitHub, you can submit a pull request to the original repository. Ensure you explain in detail what changes you've made and why.

10. **Respond to any feedback**: If you receive feedback on your PR, make sure to respond and make any changes that are requested.

11. **Celebrate your contribution**: Once your PR has been accepted, you've made an official contribution to the project! Keep your fork updated with changes in the original repository to continue contributing in the future.

Remember, your contribution can make a significant difference and help to improve the detection and treatment of brain tumors. Thank you for your collaboration!



<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
