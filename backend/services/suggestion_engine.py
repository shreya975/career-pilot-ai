class SuggestionEngine:
    """
    Generate AI-like suggestions for resume improvement
    """

    def generate(self, target_role, missing_skills, match_percentage):

        suggestions = []

        # Priority suggestions based on missing skills
        for skill in missing_skills[:5]:

            suggestions.append(
                f"Learn {skill} to improve your {target_role} readiness."
            )


        # Match percentage based suggestions
        if match_percentage >= 80:

            suggestions.append(
                "Your profile is strong. Focus on advanced projects and system design."
            )

        elif match_percentage >= 60:

            suggestions.append(
                "You are close to being job-ready. Improve missing skills and build more projects."
            )

        elif match_percentage >= 40:

            suggestions.append(
                "You have a good foundation. Focus on core backend and real-world projects."
            )

        else:

            suggestions.append(
                "You need significant improvement. Focus on fundamentals and hands-on practice."
            )


        # General suggestions
        suggestions.append(
            "Build at least 2 real-world projects."
        )

        suggestions.append(
            "Upload projects to GitHub."
        )

        suggestions.append(
            "Practice coding problems regularly."
        )

        return suggestions
