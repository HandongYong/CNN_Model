# Datasplit code

import os
import shutil
import random

# Set input and output paths
input_data_path = " your input path "
base_output_path = "your output path "

# Extract the last folder name from the input path
last_folder_name = os.path.basename(input_data_path)

# Create directories for each set
train_dir = os.path.join(base_output_path, 'train', last_folder_name)
val_dir = os.path.join(base_output_path, 'val', last_folder_name)
test_dir = os.path.join(base_output_path, 'test', last_folder_name)

# Remove directories if already exist
shutil.rmtree(train_dir, ignore_errors=True)
shutil.rmtree(val_dir, ignore_errors=True)
shutil.rmtree(test_dir, ignore_errors=True)

# Create new directories
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Get list of files in the input path
file_names = os.listdir(input_data_path)

# Shuffle the file list
random.shuffle(file_names)

# Set ratios for splitting into train and test sets
test_split_ratio = 0.2  # ratio of test set
val_split_ratio = 0.3   # ratio of validation set (30% of remaining train set)

# Calculate indices
test_split_index = int(len(file_names) * (1 - test_split_ratio))
val_split_index = int(test_split_index * (1 - val_split_ratio))

# Split the files
train_files = file_names[:val_split_index]
val_files = file_names[val_split_index:test_split_index]
test_files = file_names[test_split_index:]

# Move or copy files to respective train, val, test directories
for file in train_files:
    shutil.copy(os.path.join(input_data_path, file), os.path.join(train_dir, file))

for file in val_files:
    shutil.copy(os.path.join(input_data_path, file), os.path.join(val_dir, file))

for file in test_files:
    shutil.copy(os.path.join(input_data_path, file), os.path.join(test_dir, file))

# Print number of split files
num_train_files = len(os.listdir(train_dir))
num_val_files = len(os.listdir(val_dir))
num_test_files = len(os.listdir(test_dir))
print(f"Number of train data files: {num_train_files}")
print(f"Number of val data files: {num_val_files}")
print(f"Number of test data files: {num_test_files}")

print("Train, val, and test data split complete")
