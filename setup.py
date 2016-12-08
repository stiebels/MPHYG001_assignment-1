from setuptools import find_packages, setup

setup(name = 'greengraph',
    version = '0.8',
    description = 'Calculates the number of green pixels between two geographical locations',
    author = 'Simon Stiebellehbner',
    author_email = 'ucabsti@ucl.ac.uk',
    maintainer = 'Simon Stiebellehner',
    maintainer_email = 'ucabsti@ucl.ac.uk',
    url = 'https://github.com/stiebels/',
    packages = find_packages(exclude=['*test']),
    license = 'MIT',
    install_requires = ['numpy', 'matplotlib', 'geopy', 'requests', 'argparse'],
	scripts= ['scripts/greengraph']
    )