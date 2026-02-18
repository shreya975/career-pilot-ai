import json
from config import Config
import os


class RoadmapDataLoader:

    _resources = None
    _projects = None
    _phase_metadata = None

    @classmethod
    def load_learning_resources(cls):

        if cls._resources is None:

            path = os.path.join(Config.DATA_FOLDER, "learning_resources.json")

            with open(path, "r", encoding="utf-8") as f:
                cls._resources = json.load(f)

        return cls._resources

    @classmethod
    def load_project_suggestions(cls):

        if cls._projects is None:

            path = os.path.join(Config.DATA_FOLDER, "project_suggestions.json")

            with open(path, "r", encoding="utf-8") as f:
                cls._projects = json.load(f)

        return cls._projects

    @classmethod
    def load_phase_metadata(cls):

        if cls._phase_metadata is None:

            path = os.path.join(Config.DATA_FOLDER, "phase_metadata.json")

            with open(path, "r", encoding="utf-8") as f:
                cls._phase_metadata = json.load(f)

        return cls._phase_metadata
