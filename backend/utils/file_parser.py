import os
import pdfplumber
from docx import Document


class FileParser:

    @staticmethod
    def extract_text(file_path):

        if not os.path.exists(file_path):
            return None

        extension = file_path.split(".")[-1].lower()

        if extension == "pdf":
            return FileParser.extract_pdf(file_path)

        elif extension == "docx":
            return FileParser.extract_docx(file_path)

        elif extension == "txt":
            return FileParser.extract_txt(file_path)

        else:
            return None


    @staticmethod
    def extract_pdf(file_path):

        text = ""

        try:

            with pdfplumber.open(file_path) as pdf:

                for page in pdf.pages:

                    content = page.extract_text()

                    if content:
                        text += content + "\n"

        except Exception as e:
            print("PDF extraction error:", e)
            return None

        return text.strip()


    @staticmethod
    def extract_docx(file_path):

        text = ""

        try:

            doc = Document(file_path)

            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"

        except Exception as e:
            print("DOCX extraction error:", e)
            return None

        return text.strip()


    @staticmethod
    def extract_txt(file_path):

        try:

            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read().strip()

        except:
            return None
