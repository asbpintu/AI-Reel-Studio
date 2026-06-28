from pathlib import Path
import sys

from loguru import logger

LOG_FOLDER = Path("logs")

LOG_FOLDER.mkdir(exist_ok=True)

logger.add(
    LOG_FOLDER / "app.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
    enqueue=True,
)

logger.add(
    sys.stdout,
    level="INFO",
    enqueue=True,
)

app_logger = logger