import json
from pathlib import Path

import ollama

from tools.filesystem import FileSystemTool


PROJECT_ROOT = Path(__file__).parent.resolve()
MODEL = "qwen3.5:2b"


filesystem = FileSystemTool(PROJECT_ROOT)


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "filesystem.read_file",
            "description": "Read a text file from the project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path relative to the project root."
                    }
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "filesystem.write_file",
            "description": "Create or overwrite a text file in the project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    }
                },
                "required": ["path", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "filesystem.file_exists",
            "description": "Check whether a file exists in the project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string"
                    }
                },
                "required": ["path"]
            }
        }
    }
]


def execute_tool(name, arguments):

    print(f"\n[TOOL CALL] {name}")
    print(f"[ARGUMENTS] {arguments}")

    if name == "filesystem.read_file":
        return filesystem.read_file(
            arguments["path"]
        )

    if name == "filesystem.write_file":
        return filesystem.write_file(
            arguments["path"],
            arguments["content"]
        )

    if name == "filesystem.file_exists":
        return filesystem.file_exists(
            arguments["path"]
        )

    raise ValueError(
        f"Unknown tool: {name}"
    )


def main():

    messages = [
        {
            "role": "system",
            "content": """
            You are a software development agent.

            You have access to the project filesystem through tools.

            Use the filesystem tools whenever you need to inspect
            or modify project files.

            Do not claim that you inspected a file unless you
            actually used the filesystem tool.
            """
                    },
                    {
                        "role": "user",
                        "content": """
            Inspect the project README.md and tell me how is calculated the recuperacao function.
            Do not guess. Use the filesystem tool. Also tell me how many and which are the steps on the workflow.yml file.
            """
        }
    ]

    while True:

        response = ollama.chat(
            model=MODEL,
            messages=messages,
            tools=TOOLS
        )

        message = response["message"]

        messages.append(message)

        # LLM respondeu normalmente
        if not message.get("tool_calls"):

            print("\n[LLM RESPONSE]")
            print(message["content"])

            break

        # LLM solicitou uma ou mais tools
        for tool_call in message["tool_calls"]:

            function = tool_call["function"]

            name = function["name"]
            arguments = function["arguments"]

            result = execute_tool(
                name,
                arguments
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_name": name,
                    "content": str(result)
                }
            )


if __name__ == "__main__":
    main()