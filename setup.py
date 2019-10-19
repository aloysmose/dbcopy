from setuptools import setup

setup(
    name='dbcopy',
    version='0.1.0',
    description="Copy contents of a SQL database to another",
    url='https://github.com/occrp/dbcopy',
    author='OCCRP',
    license='MIT',
    packages=['dbcopy'],
    py_modules=['dbcopy'],
    include_package_data=True,
    install_requires=[
        'sqlalchemy',
        'stringcase',
        'click'
    ],
    extras_require={
        'postgres': [
            'psycopg2-binary',
        ]
    },
    entry_points={
        'console_scripts': [
            'dbcopy = dbcopy.cli:dbcopy'
        ],
    },
)
