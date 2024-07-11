from setuptools import find_packages, setup

setup(
    name="my_first_cli",
    version="0.0.1",
    packages=find_packages(),
    py_modules=["main", "converters", "viewers"],
    include_package_data=True,
    include_requires=["click", "tabulate"],
    entry_points={"console_scripts": ["cli=main:main_cli"]},
)
