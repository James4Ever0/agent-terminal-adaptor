from setuptools import setup

setup(
    name="termadaptor",
    version="0.0.1",
    packages=["termadaptor"],
    description="A real terminal adaptor for AI agents",
    url="https://github.com/james4ever0/agent-terminal-adaptor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license=open("LICENSE").read(),
    install_requires=open("requirements.txt").read().strip().splitlines(),
    entry_points="""
        [console_scripts]
        termadaptor=termadaptor.cli:main
    """,
)
