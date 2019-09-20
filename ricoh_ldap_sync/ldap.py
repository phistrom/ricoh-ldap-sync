from pyad.adgroup import ADGroup
import traceback

from .log import logger
from .user import User


def get_users(ldap_group_dn, scans_share_base_dir):
    group = ADGroup.from_dn(ldap_group_dn)
    members = group.get_members()
    users = []
    logger.info("Found %s members of group '%s'" % (len(members), group.name))
    for m in members:
        logger.debug("%s is a member of %s" % (m, group.name))
        try:
            user = User.from_ldap_adobject(m, scans_path=scans_share_base_dir)
            users.append(user)
        except:
            logger.error("Failed to make a user from %s. Traceback follows:\n%s" % (m, traceback.format_exc()))

    len_users = len(users)
    logger.info("Found %s users in AD." % len_users)
    users.sort()

    return users
