from setuptools import setup

with open('requirements.txt', 'r') as f:
    reqs = f.read().splitlines()

setup(
    name='triangle',
    url='https://github.com/butomo1989/triangle',
    description='Small app to check type of triangle',
    author='Budi Utomo',
    author_email='budi.ut.1989@gmail.com',
    install_requires=reqs,
    py_modules=['cli', 'utils'],
    entry_points={'console_scripts': 'triangle=triangle.cli:cli'}
)
