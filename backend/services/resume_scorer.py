import json
import os


class ResumeScorer:
    """
    Score resume and recommend best role
    """

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        roles_file = os.path.join(base_dir, "data", "job_roles.json")

        with open(roles_file, "r", encoding="utf-8") as f:
            self.job_roles = json.load(f)


    # =====================================================
    # Calculate score for one role
    # =====================================================

    def score_role(self, user_skills, role):

        required_skills = self.job_roles.get(role, [])

        if not required_skills:
            return 0

        matched = 0

        for skill in required_skills:
            if skill.lower() in user_skills:
                matched += 1

        score = int((matched / len(required_skills)) * 100)

        return score


    # =====================================================
    # Find best role
    # =====================================================

    def find_best_role(self, user_skills):

        best_role = None
        best_score = 0

        role_scores = {}

        for role in self.job_roles:

            score = self.score_role(user_skills, role)

            role_scores[role] = score

            if score > best_score:
                best_score = score
                best_role = role


        return {
            "best_role": best_role,
            "best_score": best_score,
            "all_role_scores": role_scores
        }


    # =====================================================
    # Overall resume score
    # =====================================================

    def overall_score(self, user_skills):

        result = self.find_best_role(user_skills)

        return result
