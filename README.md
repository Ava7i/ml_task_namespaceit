

# Koala Detection Using Yolov8 from images


| Version Info | [![Python](https://img.shields.io/badge/python-v3.10.0-orange)](https://www.python.org/downloads/release/python-3900/) [![Platform](https://img.shields.io/badge/Platforms-Ubuntu%2022.04.4%20LTS%2C%20win--64-navy)](https://releases.ubuntu.com/22.04/) [![Roboflow](https://img.shields.io/badge/Roboflow-v3.4.0-purple)](https://roboflow.com/) |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


### Approach:
![](https://github.com/Ava7i/ml_task_namespaceit/blob/main/Assets/ko.drawio.png)



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Overview</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
# Overview



#### Introduction: 
This repository contains a Python-based implementation for detecting koalas in images and videos using YOLOv8, a state-of-the-art object detection algorithm.
This project focuses on leveraging the power of YOLOv8, a real-time object detection system, to identify and localize koalas within images and videos. The repository provides:

- Pre-trained weights for the YOLOv8 model specifically trained to detect koalas.
- Python scripts and Jupyter notebooks for:
- Koala detection in images.
- Training the YOLOv8 model on custom koala datasets.


#### Requirements and constraints:
- pthon = 3.10.0
- Roboflow
- ultralytics

#### Architecture and components: 
The proposed system will have the following architecture and components:
<!-- ROADMAP -->
##### Raw Data:
The given dataset has 165 Jpeg files. The given dataset also contains
- .au
- .com
- .org
and so on Files.
In details: data/Raw_data/Raw_data/md
  
#### Preprocessing: Preprocessing steps
- Clean data: First I remove the .au,.com files and store only jpeg files.
- Normalization: Resize Image
- Augmentation: Brightness,hue and so on
- Preprocess with Roboflow:
- Final Dataset
#### Model
YOLOv8 is a new state-of-the-art computer vision model built by Ultralytics, the creators of YOLOv5. The YOLOv8 model contains out-of-the-box support for object detection, classification, and segmentation tasks, accessible through a Python package as well as a command line interface.

| Features |  YOLOv5	| YOLOv7	 | YOLOv8	  | Comments |
|----------|----------|----------|----------|----------|
|Accuracy   | mAP@0.5: 50.7%    |mAP@0.5: 56.1%   | mAP@0.5: 61.7%  | high mAP  |
| FPS    | 40    | 60   | 80     | High speed      |
| Model Size(Mb)  | 24.2    | 23.2     | 22.9     | Less Memory      |


#### Architectural Enhancements of YOLOv8
YOLOv8 boasts several architectural enhancements that contribute to its superior performance:

- Backbone: Utilizes the CSPDarknet53 backbone, known for its efficient balance of accuracy and speed.

- Neck: Employs the Spatial Attention Module (SAM) and Path Aggregation Network (PANet) for enhanced feature fusion.

- Head: Leverages the YOLO head with Focal Loss and Weighted-BCE Loss for improved classification and localization.

- Data Augmentation: Introduces the Hide-and-Seek augmentation technique for further data enhancement.



# Fine -Tuining
After download the pre trained yolo model I fine tune the model on given dataset.
For fine-tuining, I tested 4 different expriements
### Expriement1

```
!yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=25 imgsz=100 plots=True
batch: 8
Optimizer : SGD # other choices=['SGD', 'Adam', 'AdamW', 'RMSProp']
lr0: 0.01
```
<!-- Result -->
### Result 
- Speed: 0.1ms pre-process
- 1.0ms inference
- 0.0ms loss
-  1.0ms post-process per image
  
![](https://github.com/Ava7i/ml_task_namespaceit/blob/main/Expriements/Expriement1/train/results%20(1).png)

### Expriement2
- Adding seed
- Increased number of epochs
- Increased number of batch sizes

```
%cd {HOME}

!yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=50 imgsz=64 plots=True
seed: 1000
batch: 12
lr0: 0.01
```
<!-- Result -->
### Result 
- Speed: 0.1ms pre-process
- 1.3ms inference
- 0.0ms loss
-  1.5ms post-process per image

### Confusion Matrix of Expriement 2
  
![](https://github.com/Ava7i/ml_task_namespaceit/blob/main/Expriements/Expriement2/train/confusion_matrix%20(2).png)


### Expriement3
- Decreasing epochs size
- Add one more parameter verbose
- Seed remaining same
- Increasing Batch sizes
```
!yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=30 imgsz=100 plots=True
verbose = True
seed: 1000
batch: 32
lr0: 0.01
     
```
<!-- Result -->
### Result 
- Speed: 0.1ms pre-process
- 1.0ms inference
- 0.0ms loss
-  1.0ms post-process per image


## Prediction of Expriement 3
  
![](https://github.com/Ava7i/ml_task_namespaceit/blob/main/Expriements/Expriement3/train/val_batch0_pred%20(4).jpg)


### Expriement4

- Increasing epoch sizes

```

!yolo task=detect mode=train model=yolov8s.pt data={dataset.location}/data.yaml epochs=100 imgsz=100


```

### Result 
- Speed: 0.1ms pre-process
- 1.3ms inference
- 0.0ms loss
-  1.2ms post-process per image
- 100 epochs completed in 0.301 hours.
  
![](https://github.com/Ava7i/ml_task_namespaceit/blob/main/Expriements/Expriement4/train/R_curve%20(4).png)


# Comparison 
Above 4 expriments, now I have 4 models but lets compare models performance:


| Model | Precision | Recall | mAP |  mAP50-95 |
|----------|----------|----------|----------|----------|
| Exp 1    |   0.851       | 0.824     |  0.831    | 0.494   |
| Exp 2    | 0.969     | 0.882   |   0.935       |  0.494        |
| Exp 3    | 0.986   | 0.824    |  0.88       | 0.512      |
| Exp 4    |  0.923  | 0.824    |  0.885      | 0.505       |


 ### From the above table I choose the Exp 3 model for the interference.

### Deployment on Roboflow

```
project.version(dataset.version).deploy(model_type="yolov8", model_path=f"{HOME}/runs/detect/train3/")

```

![](https://github.com/Ava7i/ml_task_namespaceit/blob/main/Assets/Screenshot_4.png)
![](https://github.com/Ava7i/ml_task_namespaceit/blob/main/Assets/Screenshot_3.png)
![](https://github.com/Ava7i/ml_task_namespaceit/blob/main/Assets/Screenshot_2.png)

### Demo Link
https://universe.roboflow.com/nameplate/koala-ag6b3/model/1



<!-- GETTING STARTED -->
# Getting Started

### Installation

1. Clone the repo and navigate to the directory:

```bash
git@github.com:Ava7i/ml_task_namespaceit.git
cd env
```
2. Create conda environment:

```bash
conda create -n env python=3.10.0
conda activate env
```

3. Download the necessary model weights by running the bash script:

```bash
bash main.sh
```

4. Now run the docker-compose file:

```bash
docker-compose up --build
```



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This repo is created for interviw task by Namespace IT.





