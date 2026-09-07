from pathlib import Path

from agents.validator import Validator
from tools.registry import ToolRegistry

from agents.agent import Agent
from agents.skill_loader import SkillLoader

from workflow.loader import WorkflowLoader
from workflow.orchestrator import Orchestrator


PROJECT_ROOT = Path(__file__).parent.resolve()

MODEL = "qwen3.5:2b"


def main():

    # Tools

    tool_registry = ToolRegistry(
        PROJECT_ROOT
    )

    # Skills

    skill_loader = SkillLoader(
        PROJECT_ROOT
        / ".agents"
        / "skills"
    )

    # Agent

    agent = Agent(
        model=MODEL,
        tool_registry=tool_registry
    )

    # Workflow

    workflow_loader = WorkflowLoader(
        PROJECT_ROOT
        / "workflow.yml"
    )

    workflow = workflow_loader.load()


    # Validator

    validator = Validator(
        PROJECT_ROOT
    )

    # Orchestrator

    orchestrator = Orchestrator(
        workflow=workflow,
        skill_loader=skill_loader,
        agent=agent,
        validator=validator
    )

    results = orchestrator.run()

    print("\n\nWORKFLOW FINISHED")

    for result in results:

        print(
            f"\n[{result['step']}]"
        )

        print(
            result["result"]
        )


if __name__ == "__main__":
    main()