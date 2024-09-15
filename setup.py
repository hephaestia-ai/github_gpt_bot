from setuptools import setup, find_packages
import os


def read_requirements():
    requirements_path = "requirements.txt"
    if os.path.isfile(requirements_path):
        with open(requirements_path) as req:
            return req.read().splitlines()
    return []


def read_long_description():
    with open("README.md") as readme:
        return readme.read()


setup(
    name="cgai-gh-bot",
    version="0.0.1",
    description="Cowgirl AI Github GPT Bot",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Cowgirl-AI/github_gpt_bot",
    author="Tera Earlywine",
    author_email="tera@cowgirlai.tech",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=read_requirements(),
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "cgai-gh=cli.main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)