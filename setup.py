from setuptools import setup

setup(
    name = 'C2concealer',
    python_requires='>3.5.2',
    version = '1.0',
    author = 'Joseph Leon (FortyNorthSecurity.com)',
    author_email = 'jleon@fortynorthsecurity.com',
    packages = ['C2concealer'],
    entry_points = {
        'console_scripts': [
            'C2concealer = C2concealer.__main__:main'
        ]
    })