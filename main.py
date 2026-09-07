import yaml
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent
WORKFLOW_FILE = PROJECT_ROOT / "workflow.yml"
SKILLS_DIR = PROJECT_ROOT / ".agents" / "skills"


def load_workflow():
    with open(WORKFLOW_FILE, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_skill(skill_name):
    skill_file = SKILLS_DIR / skill_name / "SKILL.md"

    if not skill_file.exists():
        raise FileNotFoundError(
            f"Skill não encontrada: {skill_file}"
        )

    return skill_file.read_text(encoding="utf-8")


def main():
    """Orquestra a execução do workflow do projeto.

    Este método é o ponto central de execução: carrega a configuração do
    workflow, identifica cada etapa e garante a execução sequencial das skills
    definidas no arquivo workflow.yml.
    """
    workflow = load_workflow()

    print(f"Workflow: {workflow['name']}")
    print()

    for step in workflow["steps"]:
        skill_name = step["skill"]

        print(f"Executing skill: {skill_name}")

        skill_content = load_skill(skill_name)

        print(f"Loaded: .agents/skills/{skill_name}/SKILL.md")
        print()

        # Por enquanto apenas mostramos o conteúdo.
        print(skill_content)
        print("-" * 60)


if __name__ == "__main__":
    main()