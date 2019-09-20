from setuptools import setup

setup(
    name='ricoh-ldap-sync',
    version='0.1',
    packages=['ricoh_ldap_sync'],
    url='',
    license='MIT',
    author='Phillip Stromberg',
    author_email='phillip@strombergs.com',
    description='For creating a CSV file for Ricoh copiers from information in LDAP',
    install_requires=[
        "pyad==0.6.0",
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ricoh-sync = ricoh_ldap_sync.cli:command_line',
        ],
    },
)
