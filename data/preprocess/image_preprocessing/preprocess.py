import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

# Define the directory containing your images
img_dir = '/content/drive/MyDrive/data/ML_Engineer_Test_NameSpaceIT-20231123T191935Z-001/clean_data'

# List all files in the directory
files = os.listdir(img_dir)

# Load and resize images while preserving aspect ratio
images = []
for file in files:
    if file.endswith('.jpeg'):  # Ensure only JPEG files are considered
        img = cv2.imread(os.path.join(img_dir, file))
        resized_img = cv2.resize(img, (100,100))  # Define new_width and new_height

        # Data augmentation: Randomly apply transformations
        if np.random.rand() < 0.5:  # 50% chance of applying augmentation
            # Randomly rotate the image by 10 degrees
            angle = np.random.randint(-10, 10)
            rows, cols, _ = resized_img.shape
            rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
            resized_img = cv2.warpAffine(resized_img, rotation_matrix, (cols, rows))

            # Randomly flip the image horizontally
            if np.random.rand() < 0.5:
                resized_img = cv2.flip(resized_img, 1)

            # Adjust brightness (optional)
            brightness = np.random.uniform(0.7, 1.3)  # Random brightness factor
            resized_img = cv2.convertScaleAbs(resized_img, alpha=brightness, beta=0)

        images.append(resized_img)

# Convert the list to a numpy array
images = np.array(images)

# Split the dataset into train, validation, and test sets (70-20-10)
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# Split the data into train and temp sets
train_images, temp_images = train_test_split(images, test_size=(1 - train_ratio))

# Split the temp set into validation and test sets
val_images, test_images = train_test_split(temp_images, test_size=test_ratio / (test_ratio + val_ratio))

# Check the shapes of the sets
print("Train set shape:", train_images.shape)
print("Validation set shape:", val_images.shape)
print("Test set shape:", test_images.shape)
