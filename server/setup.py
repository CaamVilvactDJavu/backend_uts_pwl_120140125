import os

from setuptools import setup, find_packages

requires = [
    'grpcio',
    'grpcio-tools',
    'PyMySQL',
    'alembic',
    'mysql-connector-python',
    'SQLAlchemy',
]

tests_require = [
    'pytest-cov',
    'pytest',
]

setup(
    name='server',
    version='0.0',
    description='server',
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: GRPC',
    ],
    author='',
    author_email='',
    url='',
    keywords='grpc pyramid',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
)
