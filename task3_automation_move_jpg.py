
# TASK 3: Move JPG Files Automatically

import os
import shutil

# Take folder paths from user
source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

# Check whether source folder exists
if not os.path.isdir(source_folder):
    print("Source folder does not exist!")

else:
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    count = 0

    # Read files from source folder
    for filename in os.listdir(source_folder):

        if filename.lower().endswith((".jpg", ".jpeg")):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(
                destination_folder, filename
            )

            # Avoid overwriting existing files
            if os.path.exists(destination_path):
                print("Skipped:", filename)
                continue

            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
                print("Moved:", filename)
                count += 1

    print("\nAutomation completed!")
    print("Total JPG files moved:", count)
