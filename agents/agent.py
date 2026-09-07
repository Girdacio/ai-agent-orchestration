import ollama


class Agent:

    def __init__(
        self,
        model,
        tool_registry
    ):
        self.model = model
        self.tool_registry = tool_registry

    def run(self, instruction):

        messages = [
            {
                "role": "system",
                "content": """
                You are a software development agent.

                Follow the provided instructions carefully.

                Use filesystem tools whenever you need to
                inspect or modify project files.

                Never claim that you inspected or modified
                a file unless you actually used a tool.
                """
            },
            {
                "role": "user",
                "content": instruction
            }
        ]

        while True:

            response = ollama.chat(
                model=self.model,
                messages=messages,
                tools=self.tool_registry.definitions()
            )

            message = response["message"]

            messages.append(message)

            if not message.get("tool_calls"):

                return message["content"]

            for tool_call in message["tool_calls"]:

                function = tool_call["function"]

                name = function["name"]
                arguments = function["arguments"]

                print(
                    f"\n[TOOL CALL] {name}"
                )

                print(
                    f"[ARGUMENTS] {arguments}"
                )

                tool = self.tool_registry.get(
                    name
                )

                try:
                    result = tool.execute(
                        arguments
                    )

                except Exception as e:
                    result = f"Tool error: {type(e).__name__}: {e}"

                messages.append(
                    {
                        "role": "tool",
                        "tool_name": name,
                        "content": str(result)
                    }
                )