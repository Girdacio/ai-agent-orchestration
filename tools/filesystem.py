from pathlib import Path


class FileSystemTool:

    def __init__(self, project_root):
        self.project_root = Path(project_root).resolve()

    def read_file(self, path):
        file_path = self._safe_path(path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        if not file_path.is_file():
            raise ValueError(f"Not a file: {path}")

        return file_path.read_text(encoding="utf-8")

    def write_file(self, path, content):
        file_path = self._safe_path(path)

        file_path.parent.mkdir(parents=True, exist_ok=True)

        file_path.write_text(
            content,
            encoding="utf-8"
        )

    def exists(self, path):
        file_path = self._safe_path(path)

        return file_path.exists()

    def _safe_path(self, path):
        """Security boundary for file operations.
        
        Garantees that all file operations are confined within the project root directory.
        """
        target = (self.project_root / path).resolve()

        if not target.is_relative_to(self.project_root):
            raise PermissionError(
                f"Access outside project root denied: {path}"
            )

        return target