import gradio as gr
import easyocr
from docx import Document
import os
from PIL import Image
import numpy as np

# Initialize the EasyOCR reader (English)
# This model is much better for multi-line handwritten notes
reader = easyocr.Reader(['en'])

def convert_handwriting(image):
    image_np = np.array(image)
    
    # Using paragraph=True groups nearby text together, making it cleaner
    results = reader.readtext(image_np, detail=0, paragraph=True)
    
    extracted_text = "\n\n".join(results)
    
    doc = Document()
    doc.add_heading('Handwritten Note Transcription', 0)
    
    for paragraph in results:
        # Each detected block becomes a new paragraph in Word
        doc.add_paragraph(paragraph)
    
    file_path = "converted_notes.docx"
    doc.save(file_path)
    
    return extracted_text, file_path

# Gradio Interface
demo = gr.Interface(
    fn=convert_handwriting,
    inputs=gr.Image(type="pil", label="Upload Full Page of Notes"),
    outputs=[
        gr.Textbox(label="Extracted Text", lines=10),
        gr.File(label="Download Word Document")
    ],
    title="✍️ Full-Page Handwriting to Word",
    description="This version uses EasyOCR to handle multi-line notes and dense layouts."
)

if __name__ == "__main__":
    demo.launch()