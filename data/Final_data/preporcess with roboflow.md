
# Data Preprocessing with Roboflow

## Overview

This guide outlines the process of preprocessing data using Roboflow, a comprehensive platform for annotating, augmenting, and organizing datasets for this  task.

## Preprocessing Steps

1. **Data Upload**: Sign in to your Roboflow account and upload the  raw dataset containing images of Koalas. Supported formats include JPEG, PNG, among others.

2. **Annotation**: Utilize Roboflow's annotation tools to mark bounding boxes around the Koalas in  images. This step is crucial for object detection tasks.
   
  ###  In process:
  ![Image](https://github.com/Ava7i/ml_task_namespaceit/blob/dev/Assets/bounding_boxes.png)

   ### After annonating all the images:
   ![Image](https://github.com/Ava7i/ml_task_namespaceit/blob/dev/Assets/bounding_box.png)


4. **Augmentation**: Apply augmentation techniques offered by Roboflow to increase the diversity of your dataset. Augmentations like rotation, flipping, and color adjustments help enhance the model's robustness.

   ![Image](https://github.com/Ava7i/ml_task_namespaceit/blob/dev/Assets/augmentation.png)

5. **Normalization**: Standardize the images by resizing or cropping them to a consistent resolution. This ensures uniformity in the dataset, which is beneficial for training models.

     ![Image](https://github.com/Ava7i/ml_task_namespaceit/blob/dev/Assets/preprocessing.png)
   

7. **Export**: Once the preprocessing steps are completed, export the processed dataset in a format compatible.I export the dataset with yolov8 format.


   ## Dataset
   

 ![Image](https://github.com/Ava7i/ml_task_namespaceit/blob/dev/Assets/final_d.png)


