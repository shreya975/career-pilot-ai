import os
from flask import Flask, jsonify
from flask_cors import CORS

# Import config
from config import Config

# Import routes
from routes.analyze import analyze_bp
from routes.roadmap import roadmap_bp


def create_app():
    """
    Application Factory Pattern
    Production-ready Flask initialization
    """

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Enable CORS (allow frontend connection)
    CORS(app)

    # Ensure upload folder exists
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Register Blueprints
    app.register_blueprint(analyze_bp)
    app.register_blueprint(roadmap_bp)

    # Root route
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "success": True,
            "message": "SkillSync AI Backend Running",
            "version": "1.0.0"
        })

    # Global error handler
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": "Route not found"
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": "Internal server error"
        }), 500

    return app


# Run server
if __name__ == "__main__":
    app = create_app()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=Config.DEBUG
    )
