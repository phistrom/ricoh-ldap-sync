import csv
from .user import User, USER_CSV_FIELDS
from .constants import RICOH_CSV_HEADER


class RicohDialect(csv.Dialect):
    delimiter = ','
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_ALL


csv.register_dialect("ricoh", RicohDialect)


def write_users_to_csv(users, filepath):
    with open(filepath, "w") as outfile:
        outfile.write(RICOH_CSV_HEADER)
        writer = csv.DictWriter(outfile, USER_CSV_FIELDS, dialect=RicohDialect)
        writer.writeheader()
        for idx, user in enumerate(users, start=1):
            d = user.as_dict
            registration = "[%s]" % idx
            d["Index in ACLs and Groups"] = registration
            d["Registration No."] = registration
            writer.writerow(d)
