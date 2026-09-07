class Orchestrator:

    def __init__(
        self,
        workflow,
        skill_loader,
        agent
    ):
        self.workflow = workflow
        self.skill_loader = skill_loader
        self.agent = agent

    def run(self):

        results = []

        for step in self.workflow["steps"]:

            step_id = step["id"]
            skill_name = step["skill"]

            print(
                f"\n=============================="
            )

            print(
                f"STEP: {step_id}"
            )

            print(
                f"SKILL: {skill_name}"
            )

            print(
                f"=============================="
            )

            skill = self.skill_loader.load(
                skill_name
            )

            result = self.agent.run(
                skill
            )

            results.append(
                {
                    "step": step_id,
                    "result": result
                }
            )

        return results