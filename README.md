

# Koala Detection Using Yolov8 from images


| Version Info | [![Python](https://img.shields.io/badge/python-v3.10.0-orange)](https://www.python.org/downloads/release/python-3900/) [![Platform](https://img.shields.io/badge/Platforms-Ubuntu%2022.04.4%20LTS%2C%20win--64-navy)](https://releases.ubuntu.com/22.04/) [![Roboflow](https://img.shields.io/badge/Roboflow-v3.4.0-purple)](https://roboflow.com/) |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


### proposed Architecture:




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">System design of The Project</a>
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
## System design of  The Project



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






### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Result -->
# Result

### Account A
![](https://github.com/anchorblock/ACT_BOT/blob/main/Account_A/Results/DIETClassifier_confusion_matrix.png)


### Account B

![](https://github.com/anchorblock/ACT_BOT/blob/main/Account_B/results/DIETClassifier_confusion_matrix.png)


### Final outcome with fastapi



![](https://github.com/anchorblock/ACT_BOT/blob/main/image/ezgif.com-gif-maker%20(2).gif)



![](https://github.com/anchorblock/ACT_BOT/blob/main/image/Screenshot%20from%202022-12-20%2014-31-38.png)


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 


###  Larger and Diverse training data:

I used a larger and more diverse training dataset: The performance of the dietclassifier will largely depend on the quality and quantity of the training data you use. To improve the performance of the dietclassifier, I am using a larger and more diverse training dataset that contains a wide range of examples for different intents and entities. This will help the classifier learn more robust and generalizable patterns from the data, and improve its performance on unseen examples.


