import argparse
import logging
import os

from .log import logger
from .ldap import get_users
from .ricoh_csv import write_users_to_csv


def command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("group-dn",
                        help="The DN for a Group in AD that contains all users you want in the address book CSV")
    parser.add_argument("share",
                        help="The path to the Scans share where each user will have their scans sent.")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable additional logging")
    parser.add_argument("-c", "--csv", default="scanlist.csv",
                        help="Where to output the CSV file (./scanlist.csv by default)")
    parser.add_argument("-f", "--ensure-folders-exist", action="store_true",
                        help="Ensures that a folder exists in the 'share' folder specified for each user found in LDAP")
    args = parser.parse_args().__dict__
    if args["verbose"]:
        logger.setLevel(logging.DEBUG)
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled")
    _sync_to_file(args['group-dn'], args['share'], args['csv'], args['ensure_folders_exist'])


def _sync_to_file(group_dn, scans_dir, outpath, ensure_folders_exist):
    users = get_users(group_dn, scans_dir)
    write_users_to_csv(users, outpath)
    if ensure_folders_exist:
        _ensure_folders_exist(users)


def _ensure_folders_exist(users):
    for u in users:
        try:
            os.makedirs(u.folder_path)
            logger.info("Created %s" % u.folder_path)
        except (IOError, OSError):
            logger.debug("%s already exists" % u.folder_path)  # ok if already exists
