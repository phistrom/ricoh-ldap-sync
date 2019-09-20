from codecs import open
import os
from setuptools import setup
from ricoh_ldap_sync import __VERSION__

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), 'r') as infile:
    long_description = infile.read()

setup(
    name='ricoh-ldap-sync',
    version=__VERSION__,
    packages=['ricoh_ldap_sync'],
    url='https://github.com/phistrom/ricoh-ldap-sync',
    license='MIT',
    author='Phillip Stromberg',
    author_email='phillip@strombergs.com',
    description='For creating a CSV file for Ricoh copiers from information in LDAP',
    install_requires=[
        "pyad==0.6.0",
        "pywin32==225",
        "future==0.17.1",
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'ricoh-sync = ricoh_ldap_sync.cli:command_line',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown"
)
