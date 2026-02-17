import os
import re
from PyPDF2 import PdfReader
from docx import Document


class FileParser:
    """
    Production-ready file parser for resume extraction.

    Supported formats:
    - PDF
    - DOCX
    - TXT

    Features:
    - Automatic format detection
    - Text extraction
    - Text cleaning & normalization
    - Fix broken spacing from PDF encoding
    """

    # ============================================================
    # MAIN ENTRY FUNCTION
    # ============================================================

    @staticmethod
    def extract_text(file_path):
        """
        Detect file type and extract cleaned text.
        """

        if not os.path.exists(file_path):
            raise Exception("File does not exist")

        extension = file_path.split(".")[-1].lower()

        if extension == "pdf":
            raw_text = FileParser.extract_pdf(file_path)

        elif extension == "docx":
            raw_text = FileParser.extract_docx(file_path)

        elif extension == "txt":
            raw_text = FileParser.extract_txt(file_path)

        else:
            raise Exception(f"Unsupported file format: {extension}")

        cleaned_text = FileParser.clean_text(raw_text)

        return cleaned_text

    # ============================================================
    # PDF PARSER
    # ============================================================

    @staticmethod
    def extract_pdf(file_path):
        """
        Extract text from PDF file
        """

        text = ""

        try:
            reader = PdfReader(file_path)

            for page in reader.pages:
                content = page.extract_text()

                if content:
                    text += content + "\n"

        except Exception as e:
            raise Exception(f"PDF parsing failed: {str(e)}")

        return text

    # ============================================================
    # DOCX PARSER
    # ============================================================

    @staticmethod
    def extract_docx(file_path):
        """
        Extract text from DOCX file
        """

        text = ""

        try:
            document = Document(file_path)

            for paragraph in document.paragraphs:
                text += paragraph.text + "\n"

        except Exception as e:
            raise Exception(f"DOCX parsing failed: {str(e)}")

        return text

    # ============================================================
    # TXT PARSER
    # ============================================================

    @staticmethod
    def extract_txt(file_path):
        """
        Extract text from TXT file
        """

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                return file.read()

        except Exception as e:
            raise Exception(f"TXT parsing failed: {str(e)}")

    # ============================================================
    # TEXT CLEANER (VERY IMPORTANT)
    # ============================================================

    @staticmethod
    def clean_text(text):
        """
        Clean extracted text.

        Fixes:
        - Spaced letters: F i r s t → First
        - Broken words
        - Multiple spaces
        - Broken newlines
        - Encoding artifacts
        """

        if not text:
            return ""

        # Fix spaced letters: F i r s t → First
        text = re.sub(r'(?<=\w)\s(?=\w)', '', text)

        # Fix broken spacing like: "Softwar e"
        text = re.sub(r'(?<=[a-z])\s(?=[a-z])', '', text)

        # Normalize spaces
        text = re.sub(r'[ \t]+', ' ', text)

        # Normalize newlines
        text = re.sub(r'\n+', '\n', text)

        # Remove strange unicode artifacts
