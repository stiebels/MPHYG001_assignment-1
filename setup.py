from setuptools import find_packages, setup

setup(name = 'Greengraph',
    version = '0.1',
    description = 'Calculates the number of green pixels between two geographical locations',
    author = 'Simon Stiebellehbner',
    author_email = 'ucabsti@gmail.com',
    maintainer = author,
    maintainer_email = author_email,
    url = 'https://github.com/stiebels/',
    packages = find_packages(exclude=['*test']),
    license = 'MIT',
    install_requires = ['numpy', 'geopy', 'matplotlib', 'geopy', 'StringIO', 'requests', 'argparse']
	scripts= ['scripts/greengraph']
    )
