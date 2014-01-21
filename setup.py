import os
from setuptools import setup, find_packages

import {{ app_name }}


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-{{ app_name }}',
    version={{ app_name }}.__version__,
    description='Template for django standalone applications.',
    long_description=read('README.md'),
    license='BSD',
    author='byteweaver',
    author_email='contact@byteweaver.org',
    url='https://github.com/byteweaver/django-standalone-app-template',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
    ],
    test_suite='{{ app_name }}.tests',
)
