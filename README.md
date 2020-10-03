# Cam-Cop
---

### Table of Contents
- [Problem Definition](##problem-definition)

- [Proposed Solution](##Proposed Solution)

- [Existing Solution](##Existing Solution)

- [Functional Requirements](##Functional Requirements)

- [Object Detection](##Object Detection)

- [Indentifying the license plate number](##Indentifying the license plate number)

- [Credit](###Credit)


## Problem Definition
Some motorists disobey the red light without a second thought. This may be due in part to the lack of enforcement of laws that stipulate consequence for committing this offence. The system aims to assist in mitigating the disobeying of red lights and enforcement of road traffic laws. The aim of the  team was to develop a software system called “Cam Cop”. In this system ‘Cam Cop’ captures the license plate number of the motorist if s/he disobeys the authority of the red light. Cam Cop utilizes CCTV camera footage from cameras that are located at stop lights. At all stop lights, there is a white unbroken horizontal line, indicating where a motorist should not stop as the traffic light turns red. Once a motorist has significantly gone beyond this indicator at a red light, Cam Cop will be triggered and screenshots taken of the license plate of the car from the CCTV camera’s continuous feed.

---

## Proposed Solution
Cam Cop will detect license plates of vehicles that break red lights. The number on the detected license plate will be read and cross referenced to a relational database owned by the tax authority, which contains information related to that vehicle’s license plate. This includes information such as the vehicle owner’s name, address, age and photo on record. This information will be presented to the tax authority through the generation of a report. The report will include the vehicle owner’s information as well as photo evidence of the incident occurring, the level of certainty to which Cam cop believes it identified the right license plate number and the time and place of the offence committed.  If Cam Cop is unable to successfully meet the 80% threshold for license plate number identification but falls between the 50% - 79% percentile, then a report which includes any possible license plate matches along with details of the offence, which will be sent to the tax authority. A report of this nature will have a special label due to the report having a lower level of certainty and must be reviewed by a tax authority personnel to determine whether or not the license plate number taken by Cam cop matches any of the results of the database search.  If the system’s license plate number identification falls below 50%, then an image of the incident containing time, date and location will be sent to authorities instead of a report.

[Back to the top](#Cam-Cop)

---

## Existing Solution
The existing system is a prototype of the system described in the proposed solution. Due to various limitations, we were unable to build the full system proposed. In order to produce a viable project our team has created Cam Cop so it simulates the core requirements stated in the proposed solution. These requirements are the detection of license plates, and reading the license plate number. The system also displays information regarding the license plate from the image, which is queried from a database. Even though the system simulates the most of core requirements , it is  not able to take snapshots of video feed thus is not automated and current implementation may not be seen as a viable solution for the problem our team defined.

[Back to the top](#Cam-Cop)

---
## Functional Requirements
- Input image of vehicle into the system so the license plate can be detected.
- Detecting license plate from image.
- Identifying license plate number.
- Access Report

[Back to the top](#Cam-Cop)

---

## Object Detection

Cam Cop uses Tensorflow version 1.5 and the Tensorflow object detection API version 1.5, which is compatible with Python 3.6. Cam Cop is executed through an Anaconda virtual environment. Tensorflow is an open source machine learning platform. It was downloaded and installed in an Anaconda virtual environment. Tensorflow’s object detection API is a framework for solving object detection problems. Tensorflow comes pretrained, but it also gives users the ability to train it on specific objects. The API folder was downloaded onto our machines. Our team trained the Tensorflow object detection API to detect Jamaican license plates. The API was trained on over 350 images of Jamaican vehicles with their license plate being clearly visible. We split these images into two folders, these folders contained train and test data respectively.  In order to train the API on these images, boxes had to be drawn around the license plate of each image in order to obtain the coordinates of the license plate. The  API used to draw these boxes is called labelImg. The coordinates obtained after drawing the boxes were converted to XML format. All the XML files from images in the training folder and test folder were then placed in CSV files called Training and Test respectively. Two files called train.record and test.record were then generated from the CSV files. Each of these files contains the encoded image and bounding box annotation information for the corresponding train/test set. To begin training the model, several libraries had to be installed in the Anaconda virtual environment. These libraries include: 
- Pillow
- lxml
- Cython
- Contextlib2
- Jupyter
- Matplotlib
- OpenCV - python

After these libraries were installed, the object detection API was configured in the Anaconda virtual environment. We then began training the model. We used an inference graph to determine when the training was completed. The inference graph represents the model which will be used to perform the object detection. The curve on the graph had to fall below a value of 0.05 so as to indicate the sufficient training.

[Back to the top](#Cam-Cop)

---

### Identifying the license plate number

The system utilizes an Optical Character Recognition (OCR) engine called Tesseract. In order to use this engine though Python 3.6, a Python wrapper called Pytesseract had to be installed. Tesseract was downloaded on our machines, and Pytesseract was installed in the Anaconda virtual environment. Despite years of development, Tesseract is not fully accurate. For Tesseract to read images with high accuracy, these images have to be preprocessed. The preprocessing of these images includes techniques such as resizing, cropping, converting the image to grayscale, adding some type of blur to reduce noise in the image, and converting it to a binary image(applying threshold). Text also had to be of a particular size, and at a particular angle for the Tesseract OCR to provide accurate results. After the object detector scanned the image, it created a bounding box around the license plate. The coordinates of this bounding box was then used to create a cropped image. This was done to isolate the license plate from the rest of the image. The cropped image of the license plate was then resized to standardize images before preprocessing. OpenCV was then used to preprocess the image. The image was then read through Pytesseract to produce an output.
[Back to the top](#Cam-Cop)

### Credit

Credit goes to [EdjeElectronics](https://github.com/EdjeElectronics) for the [starter code](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10)

[Back to the top](#Cam-Cop)



