from tools.filesystem import FileSystemTool


class ToolRegistry:

    def __init__(self, project_root):

        self.filesystem = FileSystemTool(
            project_root
        )

        self.tools = {
            "filesystem.read_file":
                self.filesystem.read_file,

            "filesystem.write_file":
                self.filesystem.write_file,

            "filesystem.file_exists":
                self.filesystem.file_exists,
        }

    def get(self, name):

        if name not in self.tools:
            raise ValueError(
                f"Unknown tool: {name}"
            )

        return self.tools[name]