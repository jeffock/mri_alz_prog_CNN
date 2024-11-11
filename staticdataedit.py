# ONE TIME PASS OF DATA EDITING:

# Remove OAS1_ from all files
import os

# Define the root directory containing the files
root_dir = "Data"
root_mild = "Data/Mild Dementia"
root_mode = "Data/Moderate Dementia"
root_nond = "Data/Non Demented"
root_vmil = "Data/Very mild Dementia"

# Iterate through all subdirectories and files in the given directory tree
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        # Check if the file name contains "OAS1_" or "_MR1"
        if "OAS1_" in file or "_MR1" in file:
            # Create the new file name by removing the unwanted substrings
            new_name = file.replace("OAS1_", "").replace("_MR1", "")
            # Define the full paths for the current and new file names
            old_path = os.path.join(subdir, file)
            new_path = os.path.join(subdir, new_name)
            # Rename the file
            os.rename(old_path, new_path)

print("File renaming completed. All occurrences of 'OAS1_' and '_MR1' have been removed.")

# Create file system for Train/Test 
# Data      |
#           |----Mild Dementia
#           |----Moderate Dementia
#           |----Non Demented
#           |----Very mild Dementia
#
# SplitData |
#           |----train |
#           |          |---mild
#           |          |---moderate
#           |          |---non
#           |          |---vmild
#           |
#           |
#           |----test  |
#                      |---mild
#                      |---moderate
#                      |---non
#                      |---vmild

# Define the base directory for the dataset
base_dir = "SplitData"

# Define subdirectories for train and test sets
categories = ["mild", "moderate", "non", "vmild"]
subdirs = ["train", "test"]

# Create the directory structure
for subdir in subdirs:
    for category in categories:
        path = os.path.join(base_dir, subdir, category)
        os.makedirs(path, exist_ok=True)

print(f"Directory structure created under '{base_dir}'.")

# Move half the files in each x division to train/test x division
import shutil
patient_list = []
target_dir = "SplitData/train/mild"

# Mild Dementia
for file in os.listdir(root_mild):
    file_path = os.path.join(root_mild, file)
    patient_num = file[:4]
    if patient_num not in patient_list:
        patient_list.append(patient_num)
        shutil.move(file_path, target_dir)
    else:
        shutil.move(file_path, target_dir)

# Moderate Dementia

# Non Demented

# Very mild Dementia