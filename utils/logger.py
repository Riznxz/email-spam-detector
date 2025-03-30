"""import logging
from datetime import datetime
import os

# 1. Create logs directory if missing
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# 2. Configure logging with daily files (e.g., app_20230801.log)
log_filename = f"app_{datetime.now().strftime('%Y%m%d')}.log"
log_filepath = os.path.join(log_dir, log_filename)

logging.basicConfig(
    filename=log_filepath,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)
logger.info("Starting app...")  # Info message
logger.warning("Low disk space!")  # Warning
logger.error("Failed to load model!")  # Error"""