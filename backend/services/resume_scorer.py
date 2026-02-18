import json
import os


class ResumeScorer:
    """
    Score resume across all available roles inside nested job_roles.json
    """

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        roles_file = os.path.join(base_dir, "data", "job_roles.json")

        with open(roles_file, "r", encoding="utf-8") as f:
            self.job_roles = json.load(f)


    # =====================================================
    # SCORE RESUME AGAINST ALL ROLES
    # =====================================================

    def overall_score(self, user_skills):

        user_skills_set = set(skill.lower() for skill in user_skills)

        role_scores = {}

        best_role = None
        best_score = 0


        # 🔹 Loop through branches
        for branch, roles in self.job_roles.items():

            # 🔹 Loop through roles inside branch
            for role_name, role_data in roles.items():

                required_skills = role_data.get("required_skills", [])

                required_skills_set = set(skill.lower() for skill in required_skills)

                if not required_skills_set:
                    score = 0
                else:
                    matched = user_skills_set & required_skills_set
                    score = int((len(matched) / len(required_skills_set)) * 100)

                role_scores[role_name] = score

                if score > best_score:
                    best_score = score
                    best_role = role_name


        return {
            "best_role": best_role,
            "best_score": best_score,
            "all_role_scores": role_scores
        }
