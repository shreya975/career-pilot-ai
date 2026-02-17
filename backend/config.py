import os

class Config:
    """
    Production-ready configuration class
    """

    # Base directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Upload folder
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    # Data folder
    DATA_FOLDER = os.path.join(BASE_DIR, "data")

    # Max upload size (10MB)
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024

    # Allowed file extensions
    ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}

    # Debug mode
    DEBUG = True

    # Secret key (change in production)
    SECRET_KEY = "skillsync-secret-key"

    # JSON settings
    JSON_SORT_KEYS = False
