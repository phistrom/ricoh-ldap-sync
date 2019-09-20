# Ricoh LDAP Sync

Creates an address book CSV file that can be imported by Device Manager NX Lite into a Ricoh Copier.

## Install
`# pip install ricoh-ldap-sync`

## Usage
You will need the **Distinguished Name** or **DN** of a group in Active Directory where the members are users you want in the address book of the copier.
You will also need a file share or something where you want scans to go.

`$ ricoh-sync <Distinguished Name of group of members in Active Directory> <Path to folder where user folders will be scanned to> --csv addressbook.csv`

## Example

Create a CSV in this directory called **addressbook.csv** containing the users that are members of the group **Scanner Address Book** in the **Groups** OU.
The **-f** means that folders will be created for each user in the destination (`\\fileserver\Scans`) by first name. So this will create folders named `\\fileserver\Scans\Alice`, `\\fileserver\Scans\Bob`, etc.
`$ ricoh-sync "CN=Scanner Address Book,OU=Groups,DC=example,DC=com" "\\fileserver\Scans" --csv "./addressbook.csv -f`

## Requires
These packages are installed automatically by pip.
  - pyad
  - pywin32

## License
MIT
