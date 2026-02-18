import json
import os


class RoadmapGenerator:
    """
    Generate learning roadmap for missing skills
    """

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        roadmap_file = os.path.join(base_dir, "data", "roadmaps.json")

        with open(roadmap_file, "r", encoding="utf-8") as f:
            self.roadmaps = json.load(f)


    # =====================================================
    # GENERATE ROADMAP
    # =====================================================

    def generate(self, missing_skills):

        roadmap = []

        for skill in missing_skills:

            skill_lower = skill.lower()

            if skill_lower in self.roadmaps:

                roadmap.append({
                    "skill": skill_lower,
                    "steps": self.roadmaps[skill_lower]
                })

            else:

                roadmap.append({
                    "skill": skill_lower,
                    "steps": [
                        f"Learn basics of {skill}",
                        f"Practice {skill} with projects",
                        f"Build real-world applications using {skill}",
                        f"Learn advanced concepts of {skill}"
                    ]
                })

        return roadmap
