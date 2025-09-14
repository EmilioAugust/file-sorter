# 📂 File Sorter

A simple yet handy Python script that automatically organizes files in a folder by type.
No more clutter — keep your directories clean and structured! 🚀

## ✨ Features
- 🔄 Automatically sorts files into folders by type (e.g., Documents, Images, Audio, Video, Archives, Others).
- 📁 Creates folders if they don’t exist.
- ⚡ Quick and lightweight — just run and organize.
## 🛠️ Installation
Clone the repository or download the script:
```bash
git clone https://github.com/your-username/file-sorter.git
cd file-sorter

## ▶️ Usage
1. Run the script in your terminal:
```bash
python main.py
2. Enter the path to the folder you want to organize, for example:
```python
/Users/Admin/Desktop/Folder

## 📌 Example
Before:
📂 Downloads
 ┣ report.docx
 ┣ photo.png
 ┣ song.mp3
 ┣ movie.mp4
 ┗ archive.zip
After running File Sorter:
📂 Downloads
 ┣ 📁 Documents → report.docx
 ┣ 📁 Images → photo.png
 ┣ 📁 Audio → song.mp3
 ┣ 📁 Video → movie.mp4
 ┗ 📁 Archives → archive.zip

## 💡 Notes
- Files with unknown extensions will go into the Others folder.
- You can customize file type categories in the script.

📜 License
- Free to use, modify, and share.
