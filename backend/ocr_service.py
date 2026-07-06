import os
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class OCRService:

    def extract_text(self, file_path):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return self.extract_pdf(file_path)

        elif extension in [".jpg", ".jpeg", ".png"]:
            return self.extract_image(file_path)

        else:
            raise Exception("Unsupported file type")

    def extract_pdf(self, pdf_path):

        pages_text = []

        with pdfplumber.open(pdf_path) as pdf:

            print(f"\nTotal Pages : {len(pdf.pages)}")

            for i, page in enumerate(pdf.pages):

                print(f"Reading Page {i+1}")

                text = page.extract_text()

                if text:
                    print(f" Text found ({len(text)} characters)")
                    pages_text.append(text)
                else:
                    print(" No text found on this page.")
                    pages_text.append("")

        return pages_text

    def extract_image(self, image_path):

        image = Image.open(image_path)

        return pytesseract.image_to_string(image)