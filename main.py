import sys
import os
import csv
import requests

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLabel, QComboBox, QTableWidget,
    QTableWidgetItem, QHeaderView, QLineEdit
)
from PyQt6.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt, QThread, pyqtSignal


# ----------------------------
# REAL TRANSLATION FUNCTION (WORKING)
# ----------------------------
def translate_word(word, target_lang):
    try:
        url = "https://libretranslate.de/translate"

        data = {
            "q": word,
            "source": "en",
            "target": target_lang,
            "format": "text"
        }

        response = requests.post(url, data=data, timeout=10)
        return response.json()["translatedText"]

    except:
        return "ERROR"


# ----------------------------
# WORKER THREAD (NO FREEZE)
# ----------------------------
class TranslatorWorker(QThread):
    progress = pyqtSignal(int, str, str)

    def __init__(self, words, lang):
        super().__init__()
        self.words = words
        self.lang = lang

    def run(self):
        for i, word in enumerate(self.words):
            translated = translate_word(word, self.lang)
            self.progress.emit(i, word, translated)


# ----------------------------
# MAIN APP
# ----------------------------
class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SubLingo")
        self.resize(950, 650)

        self.words = []
        self.worker = None

        self.init_ui()
        self.apply_style()

    # ---------------- UI ----------------
    def init_ui(self):
        layout = QVBoxLayout()

        # Title
        title = QLabel("📘 Vocabulary Translator PRO")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        layout.addWidget(title)

        # ---------------- LANGUAGE BOX WITH FLAGS ----------------
        self.lang_box = QComboBox()

        model = QStandardItemModel()
        languages = [
            ("🇮🇷 Persian", "fa"),
            ("🇺🇸 English", "en"),
            ("🇩🇪 German", "de"),
            ("🇫🇷 French", "fr"),
            ("🇪🇸 Spanish", "es"),
            ("🇮🇹 Italian", "it"),
            ("🇷🇺 Russian", "ru"),
            ("🇹🇷 Turkish", "tr"),
            ("🇸🇦 Arabic", "ar"),
            ("🇨🇳 Chinese", "zh"),
            ("🇯🇵 Japanese", "ja"),
        ]

        for name, code in languages:
            item = QStandardItem(name)
            item.setData(code)
            model.appendRow(item)

        self.lang_box.setModel(model)
        layout.addWidget(self.lang_box)

        # ---------------- FILE BUTTON ----------------
        self.load_btn = QPushButton("📂 Select File")
        self.load_btn.clicked.connect(self.load_file)
        layout.addWidget(self.load_btn)

        # ---------------- SEARCH ----------------
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("🔍 Search...")
        self.search_box.textChanged.connect(self.search_table)
        layout.addWidget(self.search_box)

        # ---------------- BUTTONS ----------------
        self.translate_btn = QPushButton("🌍 Translate")
        self.translate_btn.clicked.connect(self.translate_words)
        layout.addWidget(self.translate_btn)

        self.export_btn = QPushButton("💾 Export CSV")
        self.export_btn.clicked.connect(self.export_table)
        layout.addWidget(self.export_btn)

        # ---------------- TABLE ----------------
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Word", "Translation"])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(self.table)

        self.setLayout(layout)

    # ---------------- STYLE ----------------
    def apply_style(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: white;
                font-size: 14px;
            }

            QLabel {
                color: #38bdf8;
            }

            QComboBox, QLineEdit {
                background-color: #1e293b;
                padding: 8px;
                border-radius: 8px;
                border: 1px solid #334155;
            }

            QPushButton {
                background-color: #3b82f6;
                padding: 10px;
                border-radius: 10px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #2563eb;
            }

            QTableWidget {
                background-color: #1e293b;
                gridline-color: #334155;
            }

            QHeaderView::section {
                background-color: #0b1220;
                padding: 6px;
                font-weight: bold;
            }
        """)

    # ---------------- LOAD FILE ----------------
    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt *.csv)"
        )

        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            self.words = [w.strip() for w in content.split(",") if w.strip()]

            file_name = os.path.basename(file_path)
            self.load_btn.setText(f"📄 {file_name}")

            self.table.setRowCount(0)

    # ---------------- TRANSLATE ----------------
    def translate_words(self):
        if not self.words:
            return

        lang = self.lang_box.currentData()
        self.table.setRowCount(0)

        self.worker = TranslatorWorker(self.words, lang)
        self.worker.progress.connect(self.add_row)
        self.worker.start()

    def add_row(self, row, word, trans):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(word))
        self.table.setItem(row, 1, QTableWidgetItem(trans))

    # ---------------- SEARCH ----------------
    def search_table(self, text):
        for row in range(self.table.rowCount()):
            w = self.table.item(row, 0).text()
            t = self.table.item(row, 1).text()

            match = text.lower() in w.lower() or text.lower() in t.lower()
            self.table.setRowHidden(row, not match)

    # ---------------- EXPORT ----------------
    def export_table(self):
        if self.table.rowCount() == 0:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save CSV", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        if not file_path.endswith(".csv"):
            file_path += ".csv"

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Word", "Translation"])

            for row in range(self.table.rowCount()):
                writer.writerow([
                    self.table.item(row, 0).text(),
                    self.table.item(row, 1).text()
                ])


# ---------------- RUN ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec())
