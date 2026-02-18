import json
import os


class SkillExtractor:
    """
    Production-ready skill extraction engine
    """

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        skills_file = os.path.join(base_dir, "data", "skills_db.json")

        with open(skills_file, "r", encoding="utf-8") as f:
            self.skills_db = json.load(f)

        # Flatten skill list
        self.all_skills = []

        for category in self.skills_db.values():
            self.all_skills.extend(category)

        # Normalize
        self.all_skills = list(set([skill.lower() for skill in self.all_skills]))


    # =====================================================
    # MAIN FUNCTION
    # =====================================================

    def extract_skills(self, text):

        if not text:
            return []

        text_lower = text.lower()

        found_skills = []

        for skill in self.all_skills:

            if skill in text_lower:
                found_skills.append(skill)

        return sorted(list(set(found_skills)))
