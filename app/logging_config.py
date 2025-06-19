import logging

def setup_logger():
    logger = logging.getLogger('app_logger')
    handler = logging.FileHandler('logs/app.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger