
# Removing Non-JPEG Files from Data
This script is designed to filter and remove non-JPEG files from a given dataset. The dataset initially contains various file types, including .jpeg, .org, .au, and .com files. 
The goal is to retain only the .jpeg files and eliminate all other formats.

# Usage
### Input Data: 
Ensure your dataset containing mixed file types (*.jpeg, *.org, *.au, *.com) is in the designated directory.

### Running the Script: 
Execute the provided script to filter out non-JPEG files and retain only the .jpeg images.
 ## Script Overview
 The script utilizes file manipulation functions to traverse through the dataset directory. It identifies and separates .jpeg files from other file formats. The non-JPEG files (.org, .au, .com, etc.) are excluded from the resulting dataset.
```
# Create the destination folder as it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

```


## Steps

### Load Dataset: 
Specify the directory path where the dataset is located.

### Filtering Process: 
Iterate through the files in the dataset directory.

### Identify JPEG Files: 
Check file extensions and segregate .jpeg files from others.

### Remove Non-JPEG Files: 
Delete or move non-JPEG files from the dataset directory.
### Save
Save the images into destination folder

## Instructions
- Download or copy the provided script into your working directory.

- Update the script's variables to point to your dataset directory.

 ## Note
Ensure to backup your dataset before executing the script, as it permanently removes non-JPEG files.

Customize the script according to your dataset structure and file naming conventions.
- Run the script in a Python environment.
- The given data contains some images .jpeg files, .org files, .au files and .com files
- So, remove the files from the data
- Only jpeg files exists
