import os

import pkg_resources
from distutils.core import setup

setup(
    name='avi_converter',
    version='1.0.0',
    packages=['avi_converter'],
    url='https://github.com/MayNiklas/p1s-avi-converter',
    author='MayNiklas',
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
            "avi-converter=avi_converter:cli",
        ],
    },
)
