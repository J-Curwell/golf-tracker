from setuptools import setup, find_packages

setup(
    name='golf_tracker',
    version='1.0.0',
    url='https://github.com/J-Curwell/golf-tracker.git',
    author='James Curwell',
    author_email='TBC',
    description='TBC',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=['pandas']
)
