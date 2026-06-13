# 📘 Vocabulary Translator PRO

A modern desktop application built with **Python + PyQt6** that helps you learn languages by translating word lists from subtitle files or text files.

---

## 🚀 Features

- 📂 Load words from `.txt` / `.csv` files  
- 🌍 Translate words into multiple languages  
- 🇮🇷 Language selector with flags  
- 📊 Clean table view (Word | Translation)  
- 🔍 Search inside translated results  
- 💾 Export results to CSV  
- ⚡ Fast background translation (QThread – no UI freeze)  
- 🎨 Modern dark UI design  
- 📄 Shows selected file name inside button  

---


---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/your-username/vocabulary-translator-pro.git
cd vocabulary-translator-pro
```

### 2. Install dependencies

```bash
pip install PyQt6 requests
```

### 3. Run application

```bash
python main.py
```

---

## 📂 File Format Example

Input file should be comma-separated words:

```
apple, book, car, computer, water
```

---

## 🌍 Supported Languages

* 🇮🇷 Persian (fa)
* 🇺🇸 English (en)
* 🇩🇪 German (de)
* 🇫🇷 French (fr)
* 🇪🇸 Spanish (es)
* 🇮🇹 Italian (it)
* 🇷🇺 Russian (ru)
* 🇹🇷 Turkish (tr)
* 🇸🇦 Arabic (ar)
* 🇨🇳 Chinese (zh)
* 🇯🇵 Japanese (ja)

---

## 🧠 How It Works

* Words are loaded from a file
* Each word is sent to a translation API (LibreTranslate)
* Translation runs in a background thread (QThread)
* Results are displayed in a table in real time

---

## ⚡ Tech Stack

* Python 3
* PyQt6 (GUI)
* Requests (API calls)
* LibreTranslate API

---

## 📤 Export Feature

You can export translated results to a CSV file:

```
Word,Translation
apple,سیب
book,کتاب
car,ماشین
```

---

## 🎯 Project Goal

This project was built for personal use to help learn vocabulary while watching subtitles and reading content.

---

## 📌 Notes

* Requires internet connection for translation
* Uses free LibreTranslate API (may have rate limits)
* UI is optimized for desktop usage

---

## 🚀 Future Improvements

* 📱 Drag & drop subtitle files (.srt support)
* 🧠 Spaced repetition (Anki-style learning system)
* 💾 Offline translation model
* ⭐ Favorite words system
* 🌙 Light/Dark theme toggle
* 📊 Progress tracking (learned words)

---

## 👨‍💻 Author

Built for personal learning and vocabulary improvement.

---
## 🤝 Contributing

Feel free to contribute!  
Open an issue, submit a pull request, or suggest new features. All contributions are welcome.

## 📄 License

MIT License – free to use and modify.
```
