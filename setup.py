from setuptools import setup
import subprocess

remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tusmehta-helloworld",
    version=remove_version,  ## 0.0.X is unstable package number
    description="Say Hello!",
    py_modules=["helloworld"],
    package_dir={"": "src"},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "blessings ~= 1.7",
    ],
    extras_require={
        "dev": ["pytest>=3.7"],
    },
    url="https://github.com/TusharMehtani/tusmehta-helloworld",
    author="Tushar Mehtani",
    author_email="tushar.mehtani@publicissapient.com",
)