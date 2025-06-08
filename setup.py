from setuptools import setup, find_packages

setup(
    name="cookie-snatcher",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    author="lsl",
    description="자동으로 웹사이트 쿠키를 수집하는 모듈",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lihuiruo101/cookie-snatcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
)
