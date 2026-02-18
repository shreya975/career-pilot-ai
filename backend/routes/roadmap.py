from flask import Blueprint, jsonify, request

from services.roadmap_generator import RoadmapGenerator


roadmap_bp = Blueprint(
    "roadmap",
    __name__,
    url_prefix="/api/roadmap"
)


# =====================================================
# Health Check
# =====================================================

@roadmap_bp.route("/health", methods=["GET"])
def health_check():

    return jsonify({
        "success": True,
        "message": "Roadmap API working"
    })


# =====================================================
# Generate Roadmap
# =====================================================

@roadmap_bp.route("/generate", methods=["POST"])
def generate_roadmap():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "success": False,
                "error": "No JSON data provided"
            }), 400

        missing_skills = data.get("missing_skills")

        if not missing_skills:

            return jsonify({
                "success": False,
                "error": "missing_skills required"
            }), 400

        generator = RoadmapGenerator()

        roadmap = generator.generate(missing_skills)

        return jsonify({
            "success": True,
            "roadmap": roadmap
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
