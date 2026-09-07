from tools.base import Tool
from tools.filesystem import FileSystemTool


class ReadFileTool(Tool):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    @property
    def name(self):
        return "filesystem.read_file"

    @property
    def description(self):
        return "Read a text file from the project."

    @property
    def parameters(self):
        return {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path relative to the project root."
                }
            },
            "required": ["path"]
        }

    def execute(self, arguments):
        return self.filesystem.read_file(
            arguments["path"]
        )


class WriteFileTool(Tool):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    @property
    def name(self):
        return "filesystem.write_file"

    @property
    def description(self):
        return "Create or overwrite a text file in the project."

    @property
    def parameters(self):
        return {
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

    def execute(self, arguments):
        return self.filesystem.write_file(
            arguments["path"],
            arguments["content"]
        )


class FileExistsTool(Tool):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    @property
    def name(self):
        return "filesystem.file_exists"

    @property
    def description(self):
        return "Check whether a file exists in the project."

    @property
    def parameters(self):
        return {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string"
                }
            },
            "required": ["path"]
        }

    def execute(self, arguments):
        return self.filesystem.file_exists(
            arguments["path"]
        )


class ListFilesTool(Tool):

    def __init__(self, filesystem):
        self.filesystem = filesystem

    @property
    def name(self):
        return "filesystem.list_files"

    @property
    def description(self):
        return "List files and directories inside a project directory."

    @property
    def parameters(self):
        return {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Directory path relative to the project root."
                }
            },
            "required": ["path"]
        }

    def execute(self, arguments):
        return self.filesystem.list_files(
            arguments.get("path", ".")
        )