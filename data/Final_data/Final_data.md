
# Final  Dataset
# Overview
This dataset is curated for task purposes, specifically focusing on the classification of Koala images. Koalas are fascinating and unique marsupials native to Australia, known for their distinctive appearance and arboreal lifestyle.

# Dataset Composition
For preparing the final dataset first, I need to clean the data because the raw dataset contains many files and images. The annotated the images. After resizing and applying augmentation techniques, I split the dataset into Three parts. The dataset comprises a total of 419 high-resolution images of Koalas. These images are divided into three subsets for different purposes:

## Training Set:
Consisting of 387 images, this set serves as the primary resource for training machine learning models. The diversity within this set ensures a robust learning experience for the model.

## Validation Set:
Comprising 16 images, the validation set is intended for fine-tuning and hyperparameter tuning during the model development phase. It helps ensure the generalization capability of the model.

## Test Set:
With 16 images, the test set is designed to evaluate the final performance of the trained model. It remains unseen by the model during training and validation, providing an unbiased assessment of its predictive accuracy.

# Dataset Structure
The images are meticulously organized into a hierarchical directory structure to facilitate ease of use. Each subset (train, valid, test) has its own dedicated folder, allowing for seamless integration into various machine learning frameworks.

```
Koala_Dataset/
|-- Train/
|   |-- Image1.jpg
|   |-- Image2.jpg
|   |-- ...
|-- Valid/
|   |-- Image1.jpg
|   |-- Image2.jpg
|   |-- ...
|-- Test/
|   |-- Image1.jpg
|   |-- Image2.jpg
|   |-- ...
    data.yml
```

# Image Characteristics
The images in this dataset showcase a variety of Koala poses, environments, and lighting conditions. It is advised to consider these factors during the model development process to enhance the model's adaptability to real-world scenarios.

# Data Annotation - Bounding Box
In addition to the image dataset, bounding box annotations have been provided for a subset of images to facilitate object localization tasks. The annotation process involves the following steps:

- Image Selection: 
An initial set of images were selected for annotation, focusing on diverse Koala poses and orientations.

- Annotation Tool:
A reliable annotation tool was utilized to mark bounding boxes around the Koalas present in the selected images.

- Annotation Process:
Trained annotators manually outlined bounding boxes around Koalas in the selected images, ensuring accuracy and consistency.

- Bounding Box Format: 
The bounding box annotations are provided in a standardized format, typically containing coordinates (x, y) for the top-left corner, width, and height of the bounding box.

The bounding box annotations are available for a subset of images in the training set, enabling object detection and localization tasks.


# Table

| Subset         | Number of Images |
|----------------|------------------|
| Training Set   | 387              |
| Validation Set | 16               |
| Test Set       | 16               |
| Total Images   | 419              |
| Given Images   | 165              |


# Dataset Links
This dataset is available on Roboflow. Direct link to download this dataset
```
https://app.roboflow.com/ds/F4uZdnz1pG?key=lI1u5FmPHw
```

Using in Google Colab
```
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="")
project = rf.workspace("nameplate").project("koala-ag6b3")
dataset = project.version(1).download("yolov8")
```

 
