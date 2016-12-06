from setuptools import find_packages, setup

setup(name = 'Greengraph',
    version = '0.2',
    description = 'Calculates the number of green pixels between two geographical locations',
    author = 'Simon Stiebellehbner',
    author_email = 'ucabsti@ucl.ac.uk',
    maintainer = 'Simon Stiebellehner',
    maintainer_email = 'ucabsti@ucl.ac.uk',
    url = 'https://github.com/stiebels/',
    packages = find_packages(exclude=['*test']),
    license = 'MIT',
    install_requires = ['numpy', 'matplotlib', 'geopy', 'requests', 'argparse'],
	scripts= ['scripts/run_greengraph.py']
    )
