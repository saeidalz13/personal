from setuptools import setup, find_packages

setup(
    name="saeid",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["saeid=saeid.wrapper_saeid.wrapper:main"],
    },
    install_requires=["pandas", "tqdm"],
)
