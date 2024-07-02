import os

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="esm_reward",
    version='0.0.1',
    description="Code from the ESM repo to give reward for esm log likelihood task",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    packages=['esm_reward']
)

