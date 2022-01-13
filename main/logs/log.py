import logging

def log():
    logging.basicConfig(filename='logs.log', level=logging.INFO)
    logging.error(f'Error happend ')
    logging.info('Info message')
    logging.debug('Debug message')