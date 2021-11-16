import logging
import pathlib

from logger.logger import log

BASE_DIR = pathlib.Path(__file__).parent.resolve()
config_file = BASE_DIR / 'config.yaml'


@log(config_file=config_file.__str__())
def test(name):
    logging.info(f"test -> {name}")




def test2():
    logging.info('Test2')


test2()

test('Bhavani')

