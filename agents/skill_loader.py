from pathlib import Path


class SkillLoader:

    def __init__(self, skills_root: Path):
        self.skills_root = skills_root.resolve()

    def load(self, skill_name: str) -> str:

        skill_file = (
            self.skills_root
            / skill_name
            / "SKILL.md"
        )

        if not skill_file.exists():
            raise FileNotFoundError(
                f"Skill not found: {skill_name}"
            )

        return skill_file.read_text(
            encoding="utf-8"
        )
