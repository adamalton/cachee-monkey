import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name="cachee-monkey",
    version="0.1",
    author="Adam Alton",
    author_email="adamalton@gmail.com",
    description="A simple library for caching the results of functions.",
    long_description=(read('README.md')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    license="MIT",
    keywords="django python cache caching",
    url='https://github.com/adamalton/cachee-monkey',
    packages=find_packages(),
    zip_safe=False,
)
