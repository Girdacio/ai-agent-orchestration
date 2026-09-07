from pathlib import Path


class Validator:

    def __init__(self, project_root: Path):
        self.project_root = project_root.resolve()

    def validate(self, validator_name):

        if validator_name == "hello-world":
            return self.validate_hello_world()

        if validator_name == "readme":
            return self.validate_readme()

        raise ValueError(
            f"Unknown validator: {validator_name}"
        )

    def validate_hello_world(self):

        implementation = (
            self.project_root
            / "hello_world.py"
        )

        test = (
            self.project_root
            / "test_hello_world.py"
        )

        errors = []

        if not implementation.exists():
            errors.append(
                "hello_world.py does not exist"
            )

        if not test.exists():
            errors.append(
                "test_hello_world.py does not exist"
            )

        return {
            "valid": len(errors) == 0,
            "errors": errors
        }

    def validate_readme(self):

        readme = (
            self.project_root
            / "README.md"
        )

        errors = []

        if not readme.exists():
            errors.append(
                "README.md does not exist"
            )

        return {
            "valid": len(errors) == 0,
            "errors": errors
        }