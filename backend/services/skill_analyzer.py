import json
import os


class SkillAnalyzer:
    """
    Analyze skill gaps between user skills and job role requirements
    """

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        roles_file = os.path.join(base_dir, "data", "job_roles.json")

        with open(roles_file, "r", encoding="utf-8") as f:
            self.job_roles = json.load(f)


    # =====================================================
    # MAIN FUNCTION
    # =====================================================

    def analyze_gap(self, user_skills, target_role):

        target_role = target_role.lower()

        if target_role not in self.job_roles:

            return {
                "error": "Role not found",
                "available_roles": list(self.job_roles.keys())
            }

        required_skills = self.job_roles[target_role]

        user_skills = [skill.lower() for skill in user_skills]

        matched_skills = []
        missing_skills = []

        for skill in required_skills:

            if skill in user_skills:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        match_percentage = int(
            (len(matched_skills) / len(required_skills)) * 100
        )

        return {
            "target_role": target_role,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "match_percentage": match_percentage
        }
