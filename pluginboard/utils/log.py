# encoding:utf-8
import logging
import logging.config

from pluginboard.settings import config


class RequireDebugFalse(logging.Filter):
    def filter(self, record):
        return not config.DEBUG


class RequireDebugTrue(logging.Filter):
    def filter(self, record):
        return config.DEBUG


def configure_logging(logging_config=None):
    """
    :param logging_config: logging config dict
    :return:
    """
    logging.config.dictConfig(config.DEFAULT_LOGGING)
    if logging_config:
        logging.config.dictConfig(logging_config)
