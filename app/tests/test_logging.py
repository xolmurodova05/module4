import os
from logging_config import setup_logger

def test_logging():
    logger = setup_logger()
    logger.info("Testing log entry")
    assert os.path.exists('logs/app.log')
