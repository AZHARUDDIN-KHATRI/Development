import os
import shutil

def organize_folder(target_directory):
    # Dictionary mapping folder names to their corresponding file extensions
    FILE_TYPES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Video": [".mp4", ".mkv", ".avi", ".mov"],
        "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
        "Scripts_and_Codes": [".py", ".js", ".html", ".css", ".cpp", ".java"]
    }

    # Verify if the provided directory exists
    if not os.path.exists(target_directory):
        print(f"Error: The path '{target_directory}' does not exist.")
        return

    print(f"Scanning target directory: {target_directory}...\n")

    # Iterate through all files in the given directory
    for filename in os.listdir(target_directory):
        source_file_path = os.path.join(target_directory, filename)

        # Skip if it is a directory instead of a file
        if os.path.isdir(source_file_path):
            continue

        # Extract file extension in lowercase
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Find the appropriate destination category
        moved = False
        for category, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                category_folder_path = os.path.join(target_directory, category)
                
                # Create the category folder if it doesn't exist yet
                if not os.path.exists(category_folder_path):
                    os.makedirs(category_folder_path)

                # Define absolute destination path
                destination_file_path = os.path.join(category_folder_path, filename)
                
                # Move the file safely
                shutil.move(source_file_path, destination_file_path)
                print(f"Moved: [ {filename} ]  --->  Folder: {category}/")
                moved = True
                break

        # If extension doesn't match any category, move to an 'Others' folder
        if not moved and file_extension:
            others_folder_path = os.path.join(target_directory, "Others")
            if not os.path.exists(others_folder_path):
                os.makedirs(others_folder_path)
            
            shutil.move(source_file_path, os.path.join(others_folder_path, filename))
            print(f"Moved: [ {filename} ]  --->  Folder: Others/")

    print("\n✓ Directory cleanup and organization complete!")

if __name__ == "__main__":
    # Provide the path of the cluttered folder you want to organize
    # Example: "C:/Users/YourName/Downloads" or just passing a local folder path "."
    path_to_clean = input("Enter the absolute path of the directory to organize: ").strip()
    organize_folder(path_to_clean)
