from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="saeid",
    version="2.0",
    packages=find_packages(),
    package_data={"saeid": [str(Path("TD", "td_hours.db"))]},
    entry_points={
        "console_scripts": ["saeid=saeid.wrapper_saeid.wrapper:main"],
    },
    install_requires=[],
)
