from utils.roadmap_data_loader import RoadmapDataLoader


class RoadmapGenerator:
    """
    Enterprise Roadmap Generator
    Fully dynamic, scalable & production-ready.
    Supports all engineering branches & 120+ skills.
    """

    def __init__(self):
        self.resources = RoadmapDataLoader.load_learning_resources()
        self.projects = RoadmapDataLoader.load_project_suggestions()
        self.phase_meta = RoadmapDataLoader.load_phase_metadata()

        # ================= FOUNDATION =================
        self.foundation_skills = {
            "python", "java", "c", "c++", "c#", "javascript", "typescript",
            "go", "rust", "sql", "data structures", "algorithms", "oop",
            "linux", "networking",
        }

        # ================= WEB / DEVELOPMENT =================
        self.development_skills = {
            "html", "css", "sass", "tailwind", "bootstrap",
            "react", "angular", "vue", "next.js",
            "node.js", "express", "flask", "django", "fastapi",
            "spring boot", "rest api", "graphql", "system design",
        }

        # ================= DATABASE =================
        self.database_skills = {
            "mysql", "postgresql", "mongodb", "redis",
        }

        # ================= AI / DATA =================
        self.ai_data_skills = {
            "machine learning", "deep learning", "natural language processing",
            "nlp", "computer vision", "tensorflow", "pytorch",
            "scikit-learn", "data science", "data analysis",
            "pandas", "numpy", "matplotlib", "seaborn",
            "power bi", "tableau",
        }

        # ================= CLOUD / DEVOPS =================
        self.cloud_skills = {
            "docker", "kubernetes", "jenkins", "ci/cd",
            "aws", "azure", "gcp", "terraform",
            "git", "github", "gitlab",
        }

        # ================= CYBERSECURITY =================
        self.security_skills = {
            "cybersecurity", "ethical hacking", "penetration testing",
            "cryptography", "wireshark", "firewalls",
        }

        # ================= CORE ENGINEERING =================
        self.core_engineering_skills = {
            "autocad", "solidworks", "catia", "ansys",
            "thermodynamics", "fluid mechanics", "heat transfer",
            "manufacturing processes", "machine design",

            "staad pro", "etabs", "sap2000", "revit",
            "structural analysis", "construction management",

            "digital electronics", "analog electronics",
            "embedded systems", "microcontrollers",
            "vlsi", "verilog", "vhdl", "fpga",

            "process design", "process simulation",

            "medical instrumentation",

            "aerodynamics", "cfd",
        }

        # ================= SOFT SKILLS =================
        self.soft_skills = {
            "problem solving", "critical thinking", "communication",
            "teamwork", "leadership", "project management",
            "time management",
        }

    # ==========================================================
    # RESOURCE HANDLING
    # ==========================================================

    def get_resources(self, skill: str):

        skill = skill.lower()

        if skill in self.resources:
            return self.resources[skill]

        return self.resources.get(
            "default_template",
            [
                "Official Documentation",
                "YouTube Beginner Guide",
                "Hands-on Project Tutorial",
            ],
        )

    # ==========================================================
    # SAFE PROJECT LOOKUP (CASE-INSENSITIVE FIX)
    # ==========================================================

    def get_projects(self, target_role: str):

        if not target_role:
            return []

        # find matching key ignoring case
        for role_key in self.projects.keys():

            if role_key.lower() == target_role.lower():

                return self.projects.get(role_key, [])

        return []

    # ==========================================================
    # PHASE CREATOR
    # ==========================================================

    def _create_phase(self, title: str, skills: set, meta_key: str):

        if not skills:
            return None

        meta = self.phase_meta.get(meta_key, {})

        return {
            "title": title,
            "estimated_time": meta.get("estimated_time", "Flexible"),
            "difficulty": meta.get("difficulty", "Varies"),
            "skills": [
                {
                    "name": skill,
                    "resources": self.get_resources(skill),
                }
                for skill in sorted(skills)
            ],
        }

    # ==========================================================
    # MAIN ROADMAP GENERATOR
    # ==========================================================

    def generate(self, target_role: str, missing_skills: list):

        missing = {skill.lower().strip() for skill in missing_skills}

        phases = []

        categorized_sets = [

            ("Foundation", missing & self.foundation_skills, "Foundation"),

            ("Core Development / Domain Skills",
             missing & self.development_skills,
             "Core Development / Domain Skills"),

            ("Database Systems",
             missing & self.database_skills,
             "Core Development / Domain Skills"),

            ("AI / Data Specialization",
             missing & self.ai_data_skills,
             "AI / Data Specialization"),

            ("Cloud & DevOps",
             missing & self.cloud_skills,
             "Cloud & DevOps"),

            ("Cybersecurity",
             missing & self.security_skills,
             "Core Development / Domain Skills"),

            ("Core Engineering Specialization",
             missing & self.core_engineering_skills,
             "Core Engineering Specialization"),

            ("Professional & Soft Skills",
             missing & self.soft_skills,
             "Professional & Soft Skills"),
        ]

        used_skills = set()

        for title, skills, meta_key in categorized_sets:

            if skills:

                used_skills |= skills

                phase = self._create_phase(title, skills, meta_key)

                if phase:
                    phases.append(phase)

        # ================= UNCATEGORIZED =================

        uncategorized = missing - used_skills

        if uncategorized:

            phase = self._create_phase(
                "Additional / Emerging Skills",
                uncategorized,
                "Core Development / Domain Skills",
            )

            if phase:
                phases.append(phase)

        # ================= PROJECT PHASE (FIXED) =================

        project_meta = self.phase_meta.get("Projects & Portfolio", {})

        phases.append(
            {
                "title": "Projects & Portfolio",
                "estimated_time": project_meta.get("estimated_time", "6–10 weeks"),
                "difficulty": project_meta.get("difficulty", "Intermediate"),
                "projects": self.get_projects(target_role),
            }
        )

        # ================= CAREER PREPARATION =================

        career_meta = self.phase_meta.get("Career Preparation", {})

        phases.append(
            {
                "title": "Career Preparation",
                "estimated_time": career_meta.get("estimated_time", "3–6 weeks"),
                "difficulty": career_meta.get("difficulty", "Intermediate"),
                "steps": [
                    "Practice technical interviews",
                    "Solve DSA problems",
                    "Prepare resume & LinkedIn",
                    "Mock interviews",
                    "Apply for internships/jobs",
                ],
            }
        )

        # ================= NUMBER PHASES =================

        numbered = [

            {"phase": f"Phase {i+1}", **phase}

            for i, phase in enumerate(phases)

        ]

        return {
            "target_role": target_role,
            "total_phases": len(numbered),
            "phases": numbered,
        }
