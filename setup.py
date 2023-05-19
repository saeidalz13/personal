from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="saeid",
    version="1.0",
    packages=find_packages(),
    package_data={
        "your-package": [
            str(Path("database", "TD_Hours.xlsx"))
        ]  # Replace 'data/*.xlsx' with the pattern matching your Excel files
    },
    entry_points={
        "console_scripts": ["saeid=saeid.wrapper_saeid.wrapper:main"],
    },
    install_requires=["pandas", "tqdm"],
)
