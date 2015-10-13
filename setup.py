from setuptools import setup, find_packages

version = '5.4.6'

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
        "sixieskel.policy>=1.1.2",
        "sixieskel.buildout>=1.5.5",
        # XXX: The theme isn't templer ready yet
        #"sixieskel.theme>=1.1.0",
        "sixieskel.karl>=1.0.4",
        "sixieskel.pyramid>=1.1",
    ],
    entry_points='',
    )
