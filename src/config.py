# src/config.py
import logging
from pathlib import Path
import os

def get_logger(name):
    # Create logs directory if missing
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        filename=log_dir / "app.log",
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    return logging.getLogger(name)