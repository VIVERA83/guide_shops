import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask_example_vivera83",
    version="0.0.26",
    author="Vivera83",
    author_email="vivera83@bk.ru",
    description="Flask, проба пера",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VIVERA83/guide_shops.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "flask_example"},
    packages=setuptools.find_packages(where="flask_example"),
    python_requires=">=3.9",
    include_package_data=True

)
