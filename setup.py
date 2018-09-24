from setuptools import setup


setup(
    name='addb',
    py_modules=['addb'],
    entry_points={
        'console_scripts': ['addb = addb:main', ],
    },
    install_requires=[],
    version='0.0.1',
)
