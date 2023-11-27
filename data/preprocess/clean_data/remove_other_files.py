
#import libraries
import os
# shutil.copyfile() is a function used to copy the contents of the source file to the destination file. It takes two arguments: the path of the source file and the path of the destination file.
import shutil

source_folder = "/content/drive/MyDrive/data/ML_Engineer_Test_NameSpaceIT-20231123T191935Z-001/ML_Engineer_Test_NameSpaceIT/"
destination_folder = "/content/drive/MyDrive/clean data/"

# Create the destination folder as it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get a list of all files in the main folder
files = os.listdir(source_folder)

# Filter out only the .jpeg files
# Given all the images are exists in .jpeg files
jpeg_files = [file for file in files if file.endswith(".jpeg")]

# Copy the .jpeg files to the destination folder
for jpeg_file in jpeg_files:
    source_path = os.path.join(source_folder, jpeg_file)
    destination_path = os.path.join(destination_folder, jpeg_file)
    shutil.copyfile(source_path, destination_path)
