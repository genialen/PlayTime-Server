import os

# Define the base directory for the PlayTime project
base_dir = '/mnt/data/PlayTime/'

# Define the desired structure of the project
project_structure = {
    "PlayTime/": [
        "main.py",  # Main application file
    ],
    "PlayTime/utils/": [
        "__init__.py",  # Module marker file
        "sunshine_manager.py",  # File for Sunshine management
        "logger.py",  # Already implemented logger
    ],
    "PlayTime/config/": [
        "default_config.json",  # Default configuration file
        "sunshine.conf",  # Sunshine configuration
    ],
    "PlayTime/sunshine/": [
        "sunshine.exe",  # Executable Sunshine file
    ],
    "PlayTime/logs/": [
        "playtime.log",  # Log file
    ],
    "PlayTime/templates/": [],  # Placeholder for future templates
}

# Create the directories and files
for folder, files in project_structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder_path, file)
        # Create empty files for now
        with open(file_path, 'w') as f:
            if file == "__init__.py":
                f.write("")  # Marker file for Python modules

# Return the created structure for verification
os.listdir(base_dir), {
    folder: os.listdir(os.path.join(base_dir, folder)) for folder in project_structure
}
