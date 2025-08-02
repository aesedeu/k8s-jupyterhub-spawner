from setuptools import setup, find_packages

setup(
    name='k8sspawner',
    version='1.0',

    packages=find_packages(),
    package_data={
        '': ['templates/*.jinja2']
    },

    author='Eugene Chernov',
    author_email='aesedeu@gmail.com',
    description='',

    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
