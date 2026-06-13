# 📘 Language Learning CSV Translator (Python)

A simple and powerful Python tool designed to help you learn new languages while watching movies or reading content.

This program takes a list of words (stored in a CSV or TXT file) and translates them into a target language, displaying each word alongside its meaning.

---

## 🚀 Features

* 📂 Read words from `.csv` or `.txt` files
* 🌍 Translate words into any target language
* 📖 Display original word + translated meaning
* 💾 Save translated results into a new file
* 🎬 Perfect for learning vocabulary from subtitles
* ⚡ Fast and easy to use

---

## 💡 Use Case

While watching movies with subtitles, you can:

1. Extract unfamiliar words
2. Save them into a file like this:

```id="a1b2c3"
hello,world,freedom,justice
```

3. Feed the file into this program
4. Get output like:

```id="d4e5f6"
hello -> سلام
world -> جهان
freedom -> آزادی
justice -> عدالت
```

---

## 📥 Input Format

You can provide input in two formats:

### 1. CSV File

```id="csv1"
hello,world,freedom
```

### 2. TXT File

```id="txt1"
hello,world,freedom
```

---

## 📤 Output Format

The program generates:

```id="out1"
word -> translation
```

Optionally saved into a file like:

```id="out2"
output.txt
```

---

## 🛠️ How It Works

1. Read file input
2. Parse words using comma delimiter
3. Send each word to translation API
4. Print results
5. Save results to file

---

## 🔧 Dependencies

Make sure you have Python installed.

Install required libraries:

```bash id="install1"
pip install requests
```

Optional (for better translation support):

```bash id="install2"
pip install googletrans==4.0.0-rc1
```

---

## ▶️ How to Run

```bash id="run1"
python main.py input.txt fa
```

Example:

```bash id="run2"
python main.py words.txt fa
```

---

## 📌 Arguments

| Argument   | Description                        |
| ---------- | ---------------------------------- |
| input file | CSV or TXT file                    |
| language   | Target language (e.g., `fa`, `en`) |

---

## 🧠 Future Improvements

* 🧾 Sentence translation support
* 🔊 Pronunciation (Text-to-Speech)
* 🧠 Spaced repetition system (SRS)
* 🖥️ GUI (Tkinter / PyQt)
* 📊 Word frequency tracking

---

## 🤝 Contributing

Feel free to fork the project and improve it!
Pull requests are welcome.

---

## 📄 License

MIT License

---

## ❤️ Motivation

This project was created to make language learning easier and more practical by integrating it with daily activities like watching movies.

---

## 👨‍💻 Author

Mehdi Rostami
