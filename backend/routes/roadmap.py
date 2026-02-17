from flask import Blueprint, jsonify

# Create Blueprint
roadmap_bp = Blueprint("roadmap", __name__, url_prefix="/api/roadmap")


@roadmap_bp.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint
    """
    return jsonify({
        "success": True,
        "message": "Roadmap API working"
    }), 200
