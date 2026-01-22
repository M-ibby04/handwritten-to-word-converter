# ✍️ Handwritten Notes to Word Converter

## 🎯 Overview
This project is an AI-powered system that converts handwritten notes into editable Microsoft Word documents (.docx). It is specifically designed to handle dense, multi-line handwritten content like academic notes.

## 🚀 Live Demo
**[Insert Your Hugging Face Space Link Here]**

## 🧠 Technical Highlights
- **Engine:** Transitioned from TrOCR to **EasyOCR** to better handle full-page layouts and prevent common hallucinations.
- **Formatting:** Uses `python-docx` for automated document generation.
- **UI:** Built using **Gradio** for a seamless, interactive user experience.

## 🛠️ How to Run Locally
1. Clone the repo: `git clone <https://github.com/M-ibby04/handwritten-to-word-converter>
2. Install dependencies: `pip install -r requirements.txt`
3. Launch app: `python app.py`