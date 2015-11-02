from distutils.core import setup

setup(
    name = 'python-crmtext',
    version = '0.1dev',
    packages = ['crmtext', ],
    author = 'Drew Engelson',
    author_email = 'drew@engelson.net',
    url = 'http://github.com/tomatohater/python-crmtext',
    license = 'GPLv3',
    description = 'A Python client for the CRMText API service.',
    long_description = 'A Python client for the CRMText API service.',
    keywords = 'python crmtext sms mms twilio api',
    install_requires = [
        'requests',
        'untangle',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
