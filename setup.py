import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mikeio",
    version="0.2.0",
    install_requires=["pythonnet", "numpy", "datetime", "pandas"],
    author="Henrik Andersson",
    author_email="jan@dhigroup.com",
    description="A package that works with the DHI dfs libraries to facilitate creating, writing and reading dfs0, dfs2, dfs3, dfsu and mesh files.",
    platform="windows_x64",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DHI/mikeio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Windows 10",
    ],
)
