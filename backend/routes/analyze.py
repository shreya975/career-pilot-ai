import os
import uuid

from flask import Blueprint, jsonify, request, current_app
from werkzeug.utils import secure_filename

from utils.file_parser import FileParser
from services.skill_extractor import SkillExtractor


# =====================================================
# Blueprint Initialization
# =====================================================

analyze_bp = Blueprint(
    "analyze",
    __name__,
    url_prefix="/api/analyze"
)


# =====================================================
# Health Check Route
# =====================================================

@analyze_bp.route("/health", methods=["GET"])
def health_check():
    """
    API health check
    """

    return jsonify({
        "success": True,
        "message": "Analyze API working"
    }), 200


# =====================================================
# Resume Upload + Text Extraction
# =====================================================

@analyze_bp.route("/upload", methods=["POST"])
def upload_resume():
    """
    Upload resume and extract text
    """

    try:

        # Check file exists
        if "file" not in request.files:
            return jsonify({
                "success": False,
                "error": "No file provided"
            }), 400

        file = request.files["file"]

        # Check filename
        if file.filename == "":
            return jsonify({
                "success": False,
                "error": "Empty filename"
            }), 400

        # Validate extension
        allowed_extensions = current_app.config["ALLOWED_EXTENSIONS"]

        extension = file.filename.split(".")[-1].lower()

        if extension not in allowed_extensions:
            return jsonify({
                "success": False,
                "error": f"Unsupported file format. Allowed: {allowed_extensions}"
            }), 400

        # Secure filename
        filename = secure_filename(file.filename)

        # Add UUID
        unique_filename = f"{uuid.uuid4()}_{filename}"

        upload_folder = current_app.config["UPLOAD_FOLDER"]

        file_path = os.path.join(upload_folder, unique_filename)

        # Save file
        file.save(file_path)

        # Extract text
        extracted_text = FileParser.extract_text(file_path)

        # Validate extracted text
        if not extracted_text or len(extracted_text.strip()) == 0:
            return jsonify({
                "success": False,
                "error": "Could not extract text from file"
            }), 400

        return jsonify({
            "success": True,
            "filename": unique_filename,
            "text": extracted_text,
            "text_length": len(extracted_text)
        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# =====================================================
# Skill Extraction Route
# =====================================================

@analyze_bp.route("/skills", methods=["POST"])
def extract_skills():
    """
    Extract skills from resume text
    """

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "error": "No JSON data provided"
            }), 400

        text = data.get("text")

        if not text:
            return jsonify({
                "success": False,
                "error": "Text field is required"
            }), 400

        extractor = SkillExtractor()

        skills = extractor.extract_skills(text)

        return jsonify({
            "success": True,
            "skills": skills,
            "count": len(skills)
        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
