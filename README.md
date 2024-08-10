# Diatomica


## Diatom Image Classification for Water Quality Monitoring

## Project Overview

This project aims to develop a deep learning-based system for classifying diatom images, which can be used for water quality monitoring. The system will be trained on a dataset of diatom images and will learn to identify different species of diatoms, which can indicate the water quality.

## Purpose

The purpose of this project is to provide an automated system for water quality monitoring using diatom image classification. This system can be used by water quality monitoring agencies, researchers, and environmental organizations to quickly and accurately identify diatom species and assess water quality.

## Dependencies

This project requires the following dependencies:

* Python 3.6 or later
* TensorFlow or PyTorch
* Jupyter Notebook
* Git

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository using Git.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Explore the dataset and data preprocessing scripts in the `data` folder.
4. Run the model training script in the `src` folder.
5. Evaluate the model performance using the evaluation script in the `src` folder.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.


**Model Description**
--------------------

This repository contains a diatom classifier model based on the MobileNet architecture. The model is designed to classify diatom images into one of five categories.

**Dataset**
------------

The model was trained on a dataset of 1000 images, which were preprocessed, augmented, and split into training, validation, and test sets.

**Preprocessing**
----------------

The dataset was preprocessed by:

* Loading the images from the dataset directory
* Resizing the images to a uniform size (224x224 pixels)
* Normalizing the pixel values to the range [0, 1]

**Augmentations**
----------------

The following augmentations were applied to the training dataset:

* Horizontal flip (50% chance)
* Random rotation between -10 and 10 degrees
* Addition of random values between -10 and 10 to each pixel (per channel, with 50% chance)
* Gaussian blur with a sigma value between 0 and 1.0

These augmentations were applied using the `imgaug` library.

**Splitting**
-------------

The preprocessed and augmented dataset was split into:

* Training set: 80% of the dataset
* Validation set: 10% of the dataset
* Test set: 10% of the dataset

**Model Architecture**
---------------------

The model uses the pre-trained MobileNet architecture as a feature extractor, followed by a global average pooling layer and a dense layer with 5 outputs (one for each class).

**Training**
------------

The model was trained using the Adam optimizer with a learning rate of 0.001. The model was trained for 20 epochs with a batch size of 32.

**Performance**
--------------

The model achieved a baseline accuracy of 0.260 on the test dataset.

**Usage**
--------

To use this model, simply download the `mobilenet_model.keras` file and load it into your preferred deep learning framework.


**Acknowledgments**
----------------

This model was developed using the [(https://www.kaggle.com/datasets/huseyingunduz/diatom-dataset)] dataset and the `imgaug` library.