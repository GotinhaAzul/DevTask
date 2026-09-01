import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)


class logs:
    '''Então, isso aqui é basicamente obsoleto. Mas, que surpresa, ela faz logs.'''
    def process(self, message):
        logger.debug(f"{message}")
    def action(self, message):
        logger.info(f"{message}")
