"""
Central logging configuration.
"""

import logging


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    return logging.getLogger(name)