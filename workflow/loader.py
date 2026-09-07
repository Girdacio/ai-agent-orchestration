from pathlib import Path

import yaml


class WorkflowLoader:

    def __init__(self, workflow_file: Path):
        self.workflow_file = workflow_file

    def load(self):

        with self.workflow_file.open(
            "r",
            encoding="utf-8"
        ) as file:

            return yaml.safe_load(file)