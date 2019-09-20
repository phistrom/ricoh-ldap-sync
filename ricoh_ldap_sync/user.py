class User(object):
    def __init__(self, first_name, last_name, email, scans_path):
        self.first_name = first_name
        self.last_name = last_name
        if not email:
            email = ""
        self.email = email
        self.scans_path = scans_path

    @classmethod
    def from_ldap_dict(cls, d, scans_path):
        return cls(first_name=d["givenName"], last_name=d["sn"], email=d["mail"], scans_path=scans_path)

    @classmethod
    def from_ldap_adobject(cls, ad_object, scans_path):
        return cls(first_name=ad_object.givenName, last_name=ad_object.sn, email=ad_object.mail, scans_path=scans_path)

    @property
    def name(self):
        try:
            return "%s %s" % (self.first_name, self.last_name[0])
        except (IndexError, TypeError):
            return self.first_name

    @property
    def title_1(self):
        try:
            letter = self.first_name[0].upper()
            if letter < "C":
                return 1
            elif letter < "E":
                return 2
            elif letter < "G":
                return 3
            elif letter < "I":
                return 4
            elif letter < "L":
                return 5
            elif letter < "O":
                return 6
            elif letter < "R":
                return 7
            elif letter < "U":
                return 8
            elif letter < "X":
                return 9
            else:
                return 10
        except:
            return ""

    @property
    def folder_path(self):
        return r"%s\%s" % (self.scans_path, self.first_name)

    @property
    def as_dict(self):
        return {
            "Index in ACLs and Groups": "[]",
            "Name": "[%s]" % self.name,
            "Set General Settings": "[1]",
            "Set Registration No.": "[0]",
            "Registration No.": "[]",
            "Entry Type": "[U]",
            "Phonetic Name": "[]",
            "Display Name": "[%s]" % self.name,
            "Display Priority": "[5]",
            "Set Title Settings": "[1]",
            "Title 1": "[%s]" % self.title_1,
            "Title 2": "[]",
            "Title 3": "[]",
            "Title Freq.": "[1]",
            "Set User Code Settings": "[0]",
            "User Code": "[]",
            "Set Auth. Info Settings": "[1]",
            "Device Login User Name": "[]",
            "Device Login Password": "[]",
            "Device Login Password Encoding": "[omitted]",
            "SMTP Authentication": "[0]",
            "SMTP Authentication Login User Name": "[]",
            "SMTP Authentication Login Password": "[]",
            "SMTP Authentication Password Encoding": "[omitted]",
            "Folder Authentication": "[0]",
            "Folder Authentication Login User Name": "[]",
            "Folder Authentication Login Password": "[]",
            "Folder Authentication Password Encoding": "[omitted]",
            "LDAP Authentication": "[0]",
            "LDAP Authentication Login User Name": "[]",
            "LDAP Authentication Login Password": "[]",
            "LDAP Authentication Password Encoding": "[omitted]",
            "Set Access Control Settings": "[0]",
            "Can Use B/W Copy": "[0]",
            "Can Use Single Color Copy": "[0]",
            "Can Use Two Color Copy": "[0]",
            "Can Use Full Color Copy": "[0]",
            "Can Use Auto Color Copy": "[0]",
            "Can Use B/W Print": "[0]",
            "Can Use Color Print": "[0]",
            "Can Use Scanner": "[]",
            "Can Use Fax": "[]",
            "Can Use Document Server": "[]",
            "Maximum of Print Usage Limit": "[-1]",
            "Set Email/Fax Settings": "[%s]" % (1 if self.email else 0),
            "Fax Destination": "[]",
            "Fax Line Type": "[g3]",
            "International Fax Transmission Mode": "[]",
            "E-mail Address": "[%s]" % self.email,
            "Ifax Address": "[]",
            "Ifax Enable": "[0]",
            "Direct SMTP": "[]",
            "Ifax Direct SMTP": "[]",
            "Fax Header": "[1]",
            "Label Insertion 1st Line (Selection)": "[]",
            "Label Insertion 2nd Line (String)": "[]",
            "Label Insertion 3rd Line (Standard Message)": "[0]",
            "Set Folder Settings": "[1]",
            "Folder Protocol": "[0]",
            "Folder Port No.": "[21]",
            "Folder Server Name": "[]",
            "Folder Path": "[%s]" % self.folder_path,
            "Folder Japanese Character Encoding": "[us-ascii]",
            "Set Protection Settings": "[1]",
            "Is Setting Destination Protection": "[1]",
            "Is Protecting Destination Folder": "[0]",
            "Is Setting Sender Protection": "[0]",
            "Is Protecting Sender": "[0]",
            "Sender Protection Password": "[]",
            "Sender Protection Password Encoding": "[omitted]",
            "Access Privilege to User": "[]",
            "Access Privilege to Protected File": "[]",
            "Set Group List Settings": "[1]",
            "Groups": "[]",
            "Set Counter Reset Settings": "[0]",
            "Enable Plot Counter Reset": "[]",
            "Enable Fax Counter Reset": "[]",
            "Enable Scanner Counter Reset": "[]",
            "Enable User Volume Counter Reset": "[]"
        }

    def __lt__(self, other):
        return self.first_name < other.first_name


USER_CSV_FIELDS = (
    "Index in ACLs and Groups",
    "Name",
    "Set General Settings",
    "Set Registration No.",
    "Registration No.",
    "Entry Type",
    "Phonetic Name",
    "Display Name",
    "Display Priority",
    "Set Title Settings",
    "Title 1",
    "Title 2",
    "Title 3",
    "Title Freq.",
    "Set User Code Settings",
    "User Code",
    "Set Auth. Info Settings",
    "Device Login User Name",
    "Device Login Password",
    "Device Login Password Encoding",
    "SMTP Authentication",
    "SMTP Authentication Login User Name",
    "SMTP Authentication Login Password",
    "SMTP Authentication Password Encoding",
    "Folder Authentication",
    "Folder Authentication Login User Name",
    "Folder Authentication Login Password",
    "Folder Authentication Password Encoding",
    "LDAP Authentication",
    "LDAP Authentication Login User Name",
    "LDAP Authentication Login Password",
    "LDAP Authentication Password Encoding",
    "Set Access Control Settings",
    "Can Use B/W Copy",
    "Can Use Single Color Copy",
    "Can Use Two Color Copy",
    "Can Use Full Color Copy",
    "Can Use Auto Color Copy",
    "Can Use B/W Print",
    "Can Use Color Print",
    "Can Use Scanner",
    "Can Use Fax",
    "Can Use Document Server",
    "Maximum of Print Usage Limit",
    "Set Email/Fax Settings",
    "Fax Destination",
    "Fax Line Type",
    "International Fax Transmission Mode",
    "E-mail Address",
    "Ifax Address",
    "Ifax Enable",
    "Direct SMTP",
    "Ifax Direct SMTP",
    "Fax Header",
    "Label Insertion 1st Line (Selection)",
    "Label Insertion 2nd Line (String)",
    "Label Insertion 3rd Line (Standard Message)",
    "Set Folder Settings",
    "Folder Protocol",
    "Folder Port No.",
    "Folder Server Name",
    "Folder Path",
    "Folder Japanese Character Encoding",
    "Set Protection Settings",
    "Is Setting Destination Protection",
    "Is Protecting Destination Folder",
    "Is Setting Sender Protection",
    "Is Protecting Sender",
    "Sender Protection Password",
    "Sender Protection Password Encoding",
    "Access Privilege to User",
    "Access Privilege to Protected File",
    "Set Group List Settings",
    "Groups",
    "Set Counter Reset Settings",
    "Enable Plot Counter Reset",
    "Enable Fax Counter Reset",
    "Enable Scanner Counter Reset",
    "Enable User Volume Counter Reset"
)
