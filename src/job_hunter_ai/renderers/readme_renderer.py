"""
README rendering engine.

Responsible only for generating README.md from a markdown template.
"""

from __future__ import annotations

from pathlib import Path


class ReadmeRenderer:
    """Render README.md from a markdown template."""

    def __init__(
        self,
        template_path: str = "templates/README.template.md",
        output_path: str = "README.md",
    ):
        self.template_path = Path(template_path)
        self.output_path = Path(output_path)

    def render(self, context: dict) -> None:
        """
        Render README.md from template.
        """

        template = self._load_template()
        content = self._replace_placeholders(template, context)
        self._write_file(content)

    def _load_template(self) -> str:
        """
        Read markdown template.
        """

        return self.template_path.read_text(encoding="utf-8")

    def _replace_placeholders(
        self,
        template: str,
        context: dict,
    ) -> str:
        """
        Replace {{PLACEHOLDER}} values.
        """

        for key, value in context.items():
            template = template.replace(
                f"{{{{{key}}}}}",
                str(value),
            )

        return template

    def _write_file(
        self,
        content: str,
    ) -> None:
        """
        Save generated README.
        """

        self.output_path.write_text(
            content,
            encoding="utf-8",
        )