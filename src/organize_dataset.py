import os
import shutil

SOURCE_DIR = "dataset_raw"
TARGET_DIR = "dataset"

moods = ["happy", "sad", "calm", "anxiety"]

for folder in os.listdir(SOURCE_DIR):
    folder_path = os.path.join(SOURCE_DIR, folder)

    if not os.path.isdir(folder_path):
        continue

    folder_lower = folder.lower()

    for mood in moods:
        if mood in folder_lower:
            dest_folder = os.path.join(TARGET_DIR, mood)
            os.makedirs(dest_folder, exist_ok=True)

            # 🔥 Walk through all subfolders
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    src_file = os.path.join(root, file)
                    try:
                        shutil.copy(src_file, dest_folder)
                    except Exception as e:
                        print(f"Skipped {src_file}: {e}")

print("Dataset organized successfully!")