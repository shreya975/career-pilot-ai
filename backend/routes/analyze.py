import os
import uuid

from flask import Blueprint, jsonify, request, current_app
from werkzeug.utils import secure_filename

# Utils
from utils.file_parser import FileParser

# Services
from services.skill_extractor import SkillExtractor
from services.skill_analyzer import SkillAnalyzer
from services.roadmap_generator import RoadmapGenerator
from services.resume_scorer import ResumeScorer
from services.suggestion_engine import SuggestionEngine


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
    return jsonify({
        "success": True,
        "message": "Analyze API working"
    }), 200


# =====================================================
# Resume Upload + Text Extraction
# =====================================================

@analyze_bp.route("/upload", methods=["POST"])
def upload_resume():

    try:

        if "file" not in request.files:
            return jsonify({
                "success": False,
                "error": "No file provided"
            }), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({
                "success": False,
                "error": "Empty filename"
            }), 400


        allowed_extensions = current_app.config["ALLOWED_EXTENSIONS"]

        extension = file.filename.split(".")[-1].lower()

        if extension not in allowed_extensions:
            return jsonify({
                "success": False,
                "error": f"Unsupported file format. Allowed: {allowed_extensions}"
            }), 400


        filename = secure_filename(file.filename)

        unique_filename = f"{uuid.uuid4()}_{filename}"

        upload_folder = current_app.config["UPLOAD_FOLDER"]

        file_path = os.path.join(upload_folder, unique_filename)

        file.save(file_path)


        extracted_text = FileParser.extract_text(file_path)

        if not extracted_text:
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
                "error": "Text field required"
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


# =====================================================
# Skill Gap Analysis Route
# =====================================================

@analyze_bp.route("/gap", methods=["POST"])
def analyze_gap():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "error": "No JSON data provided"
            }), 400

        user_skills = data.get("skills")
        target_role = data.get("target_role")

        if not user_skills or not target_role:
            return jsonify({
                "success": False,
                "error": "skills and target_role required"
            }), 400


        analyzer = SkillAnalyzer()

        result = analyzer.analyze_gap(user_skills, target_role)


        return jsonify({
            "success": True,
            "analysis": result
        }), 200


    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# =====================================================
# FULL PIPELINE API WITH SCORING + SUGGESTIONS
# =====================================================

@analyze_bp.route("/full", methods=["POST"])
def full_analysis():

    try:

        # Validate file
        if "file" not in request.files:
            return jsonify({
                "success": False,
                "error": "No file uploaded"
            }), 400

        file = request.files["file"]

        target_role = request.form.get("target_role")

        if not target_role:
            return jsonify({
                "success": False,
                "error": "target_role required"
            }), 400


        # Validate extension
        allowed_extensions = current_app.config["ALLOWED_EXTENSIONS"]

        extension = file.filename.split(".")[-1].lower()

        if extension not in allowed_extensions:
            return jsonify({
                "success": False,
                "error": "Unsupported file format"
            }), 400


        # Save file
        filename = secure_filename(file.filename)

        unique_filename = f"{uuid.uuid4()}_{filename}"

        upload_folder = current_app.config["UPLOAD_FOLDER"]

        file_path = os.path.join(upload_folder, unique_filename)

        file.save(file_path)


        # STEP 1: Extract text
        text = FileParser.extract_text(file_path)

        if not text:
            return jsonify({
                "success": False,
                "error": "Text extraction failed"
            }), 400


        # STEP 2: Extract skills
        extractor = SkillExtractor()

        skills = extractor.extract_skills(text)


        # STEP 3: Analyze skill gap using Member 1 analyzer
        analyzer = SkillAnalyzer()

        gap_analysis = analyzer.analyze_gap(skills, target_role)


        missing_skills = gap_analysis.get("missing_skills", [])


        # STEP 4: Generate roadmap using Member 1 roadmap generator
        generator = RoadmapGenerator()

        roadmap = generator.generate(target_role, missing_skills)



        # STEP 5: Score resume
        scorer = ResumeScorer()
        score_result = scorer.overall_score(skills)

        resume_score = score_result["best_score"]
        best_role = score_result["best_role"]
        role_scores = score_result["all_role_scores"]


        # STEP 6: Generate suggestions
        suggestion_engine = SuggestionEngine()

        suggestions = suggestion_engine.generate(
            target_role,
            missing_skills,
            gap_analysis.get("match_score", 0)
        )


        # FINAL RESPONSE
        return jsonify({

            "success": True,

            "filename": unique_filename,

            "target_role": target_role,

            "extracted_skills": skills,

            "resume_score": resume_score,

            "best_role": best_role,

            "role_scores": role_scores,

            "gap_analysis": gap_analysis,

            "roadmap": {
    "phases": roadmap,
    "total_phases": len(roadmap),
    "completion_estimate": f"{len(roadmap) * 2}–{len(roadmap) * 4} weeks"
},
            
            "career_insights": {
    "recommended_role": target_role,
    "market_demand": "High",
    "difficulty": "Moderate",
    "estimated_job_readiness": f"{100 - gap_analysis.get('match_score', 0)}% remaining"
},
            
            

            "suggestions": suggestions,

            "summary": {
                "skills_found": len(skills),
                "missing_skills": len(missing_skills),
                "match_score": gap_analysis.get("match_score", 0),
                "resume_score": resume_score
            }

        }), 200


    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
  
@analyze_bp.route("/flexible", methods=["POST"])
def flexible_analysis():

    try:

        skills = []
        target_role = None


        # OPTION 1: Resume upload
        if "file" in request.files:

            file = request.files["file"]

            filename = secure_filename(file.filename)

            unique_filename = f"{uuid.uuid4()}_{filename}"

            file_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                unique_filename
            )

            file.save(file_path)

            text = FileParser.extract_text(file_path)

            extractor = SkillExtractor()

            skills = extractor.extract_skills(text)


        # OPTION 2: Manual skills input
        if "skills" in request.form:

            manual_skills = request.form.get("skills")

            skills = [
                skill.strip().lower()
                for skill in manual_skills.split(",")
            ]


        # OPTION 3: Target role
        target_role = request.form.get("target_role")


        # STEP 1: If no skills → assume beginner
        if not skills:
            skills = []


        # STEP 2: Find best role automatically if not provided
        scorer = ResumeScorer()

        score_result = scorer.overall_score(skills)

        best_role = score_result["best_role"]

        if not target_role:
            target_role = best_role


        # STEP 3: Analyze gap
        analyzer = SkillAnalyzer()

        gap = analyzer.analyze_gap(skills, target_role)

        missing_skills = gap.get("missing_skills", [])


        # STEP 4: Generate roadmap
        generator = RoadmapGenerator()

        roadmap = generator.generate(target_role, missing_skills)


        # STEP 5: Suggestions
        suggestion_engine = SuggestionEngine()

        suggestions = suggestion_engine.generate(
            target_role,
            missing_skills,
            gap.get("match_score", 0)
        )


        return jsonify({

            "success": True,

            "input": {
                "skills": skills,
                "target_role": target_role
            },

            "profile": {
                "best_role": score_result["best_role"],
                "resume_score": score_result["best_score"],
                "match_score": gap.get("match_score", 0)
            },

            "gap_analysis": gap,

            "roadmap": roadmap,

            "suggestions": suggestions,

            "role_scores": score_result["all_role_scores"]

        })


    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
