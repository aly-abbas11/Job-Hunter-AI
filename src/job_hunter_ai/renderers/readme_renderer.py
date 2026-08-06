"""
README template renderer.
"""

from pathlib import Path


class ReadmeRenderer:
    """Render README from template."""

    TEMPLATE = Path("templates/README.template.md")
    OUTPUT = Path("README.md")

    @classmethod
    def render(cls, context: dict[str, str]) -> None:

        template = cls.TEMPLATE.read_text(encoding="utf-8")

        for key, value in context.items():
            template = template.replace(
                "{{" + key + "}}",
                str(value),
            )

        cls.OUTPUT.write_text(
            template,
            encoding="utf-8",
        )