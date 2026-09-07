from tools.filesystem import FileSystemTool

from tools.filesystem_tools import (
    ReadFileTool,
    WriteFileTool,
    FileExistsTool,
)


class ToolRegistry:

    def __init__(self, project_root):

        filesystem = FileSystemTool(
            project_root
        )

        self.tools = {

            "filesystem.read_file":
                ReadFileTool(filesystem),

            "filesystem.write_file":
                WriteFileTool(filesystem),

            "filesystem.file_exists":
                FileExistsTool(filesystem),
        }

    def get(self, name):

        if name not in self.tools:
            raise ValueError(
                f"Unknown tool: {name}"
            )

        return self.tools[name]

    def definitions(self):

        return [
            tool.definition()
            for tool in self.tools.values()
        ]