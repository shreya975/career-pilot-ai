import json
import os


class SkillAnalyzer:
    """
    Analyze skill gaps between user skills and job role requirements
    Supports nested structure:
    Branch → Role → required_skills
    """

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        roles_file = os.path.join(base_dir, "data", "job_roles.json")

        with open(roles_file, "r", encoding="utf-8") as f:
            self.job_roles = json.load(f)


    # =====================================================
    # MAIN FUNCTION
    # =====================================================

    def analyze_gap(self, user_skills, target_role):

        # Normalize input
        target_role = target_role.strip().lower()

        matched_role = None
        matched_branch = None
        required_skills = []


        # =====================================================
        # SEARCH ROLE INSIDE ALL BRANCHES
        # =====================================================

        for branch, roles in self.job_roles.items():

            for role_name, role_data in roles.items():

                if role_name.lower() == target_role:

                    matched_role = role_name
                    matched_branch = branch
                    required_skills = role_data.get("required_skills", [])
                    break

            if matched_role:
                break


        # =====================================================
        # ROLE NOT FOUND
        # =====================================================

        if not matched_role:

            return {
                "error": "Role not found",
                "available_roles": [
                    role_name
                    for branch in self.job_roles.values()
                    for role_name in branch.keys()
                ]
            }


        # =====================================================
        # CALCULATE MATCH
        # =====================================================

        user_skills_set = set(skill.lower() for skill in user_skills)

        required_skills_set = set(skill.lower() for skill in required_skills)

        matched_skills = list(user_skills_set & required_skills_set)

        missing_skills = list(required_skills_set - user_skills_set)


        # Avoid division by zero
        if len(required_skills_set) == 0:
            match_score = 0
        else:
            match_score = int(
                (len(matched_skills) / len(required_skills_set)) * 100
            )


        # =====================================================
        # RETURN RESULT
        # =====================================================

        return {
            "branch": matched_branch,
            "target_role": matched_role,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "match_score": match_score
        }
