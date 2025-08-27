import os
from pathlib import Path
import shutil

categories_dict = {
    "Documents": [".docx", ".pdf", ".txt", ".doc", ".xlsx", ".pptx"],
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".heif"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".mpeg", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Web Page": [".html"],
}

other_categ = "Other"

def main():
    try:
        input_path = input("📂 Your directory (e.g. /Users/Admin/Desktop/Folder): ").title()
        os.chdir(input_path)
        print(f"📂 Sorting files in: {input_path}")
        for file in Path().iterdir():
            if file.is_file():
                for category, extensions in categories_dict.items():
                    if file.suffix.lower() in extensions:
                        dir_path = Path(category)
                        dir_path.mkdir(exist_ok=True)
                        shutil.move(file, dir_path)
            if file.is_file():
                if not file.suffix.lower() in categories_dict.values():
                    other_path = Path(other_categ)
                    other_path.mkdir(exist_ok=True)
                    shutil.move(file, other_path)
        print("✅ Files have been sorted!")

    except FileNotFoundError:
        print(f"❌ Directory not found: {input_path}")

if __name__ == '__main__':
    main()