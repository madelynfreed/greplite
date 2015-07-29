try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Rebuild Grep',
	'author': 'Madelyn Freed',
	'url': 'URL to get to it',
	'download_url': 'where to download it',
	'author_email': 'madelyn.freed@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['rebuildgrep'],
	'scripts': ['bin/logfind'],
	'name': 'rebuildgrep'
}

setup(**config)