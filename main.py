import yaml
import ollama

from pathlib import Path


PROJECT_ROOT = Path(__file__).parent
WORKFLOW_FILE = PROJECT_ROOT / "workflow.yml"
SKILLS_DIR = PROJECT_ROOT / ".agents" / "skills"

MODEL = "qwen3.5:2b"


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


def execute_skill(skill_name, previous_result=None):

    skill = load_skill(skill_name)

    prompt = f"""
        You are executing a project skill.

        Project root:
        {PROJECT_ROOT}

        Skill:
        {skill}

        Previous step result:
        {previous_result or "None"}

        Execute the instructions defined by the skill.

        You are allowed to inspect and modify the project files
        when necessary.

        When finished, provide a concise summary of what you did.
    """

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

def main():
    """Orquestra a execução do workflow do projeto.

    Este método é o ponto central de execução: carrega a configuração do
    workflow, identifica cada etapa e garante a execução sequencial das skills
    definidas no arquivo workflow.yml.
    """
    workflow = load_workflow()

    print(f"Starting workflow: {workflow['name']}")
    print()

    previous_result = None

    for index, step in enumerate(workflow["steps"], start=1):

        skill_name = step["skill"]

        print(f"[{index}] Executing: {skill_name}")

        result = execute_skill(
            skill_name,
            previous_result
        )

        print(result)
        print()
        print("-" * 70)
        print()

        previous_result = result

    print("Workflow completed.")


if __name__ == "__main__":
    main()