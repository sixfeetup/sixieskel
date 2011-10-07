from setuptools import setup, find_packages

version = '5.0'

setup(
    name='sixieskel',
    version=version,
    description="",
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='web zope command-line skeleton project',
    author='Six Feet Up, Inc.',
    author_email='info@sixfeetup.com',
    url='http://www.sixfeetup.com',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "sixieskel.policy",
        #"sixieskel.buildout",
    ],
    entry_points='',
    )
