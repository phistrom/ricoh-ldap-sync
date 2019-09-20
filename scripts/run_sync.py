import logging
from ricoh_ldap_sync import command_line, logger


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    logging.basicConfig()
    command_line()
