class Orchestrator:

    def __init__(
        self,
        workflow,
        skill_loader,
        agent,
        validator
    ):
        self.workflow = workflow
        self.skill_loader = skill_loader
        self.agent = agent
        self.validator = validator

    def run(self):

        results = []

        for step in self.workflow["steps"]:

            step_id = step["id"]
            skill_name = step["skill"]
            validator_name = step.get("validator")

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

            validation = self.validator.validate(
                validator_name
            )

            print("\nVALIDATION:")

            print(validation)

            results.append(
                {
                    "step": step_id,
                    "result": result,
                    "validation": validation
                }
            )

        return results