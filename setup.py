import sys
from setuptools import setup, find_packages

requires = [
    'requests>=2.18.4',
    'tqdm>=3.8.0'
]

if sys.version_info < (3, 2):
    requires.append('futures==2.2')
    requires.append('configparser')

setup(
    name='instagram-scraper',
    version='1.0.1',
    description=("instagram-scraper is a command-line application written in Python"
                 " that scrapes and downloads an instagram user\'s photos and videos. Use responsibly."),
    url='https://github.com/buluma/instagram-scraper',
    download_url='https://github.com/buluma/instagram-scraper/tarball/1.10.4',
    author='Michael Buluma',
    author_email='me@buluma.co.ke',
    maintainer='Shadow Walker',
    maintainer_email='me@buluma.co.ke',
    license='Public domain',
    packages=find_packages(exclude=['tests']),
    install_requires=requires,
    entry_points={
        'console_scripts': ['instagram-scraper=instagram_scraper.app:main'],
    },
    test_suite='nose.collector',
    zip_safe=False,
    keywords=['instagram', 'scraper', 'download', 'media', 'photos', 'videos']
)