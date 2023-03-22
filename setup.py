from setuptools import find_packages
from setuptools import setup

setup(
    name="bingpython",
    version="0.0.19",
    license="GNU General Public License v2.0",
    author="Ali Can Gönüllü",
    author_email="alicangonullu@yahoo.com",
    description="Bing AI Chat API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/alicangnll/BingGPT-Python",
    project_urls={"Bug Report": "https://github.com/alicangnll/BingGPT-Python/issues/new"},
    install_requires=[
        "asyncio",
        "requests",
        "websockets",
        "rich",
        "certifi",
        "uuid"
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["BingPython"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)