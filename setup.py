import pathlib

from setuptools import setup, find_packages


def parse_readme() -> str:
    file_path = pathlib.Path("README.md")
    if not file_path.is_file():
        return ""

    with open(file_path, encoding="utf-8") as fh:
        return fh.read()


def parse_requirements() -> list[str]:
    file_path = pathlib.Path("requirements/base.txt")
    if not file_path.is_file():
        return []

    with open(file_path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name="vkvideo_gui_bot",
    version="1.0.0",
    author="Kostya12rus",
    description="Приложение на Python для авто просмотра стримеров VKVideo",
    long_description=parse_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kostya12rus/vkvideo_gui_bot",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "app_vkvideo.monitoring": ["*.json"],
    },
    install_requires=parse_requirements(),
    entry_points={
        "console_scripts": [
            "vkvideo_gui_bot_gui=app_vkvideo.run:run",
            "vkvideo_gui_bot_console=app_vkvideo.run_console:run",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    license="MIT",
    keywords="desktop application vkvideo bot gui",
    project_urls={
        "Bug Tracker": "https://github.com/Kostya12rus/vkvideo_gui_bot/issues",
        "Documentation": "https://github.com/Kostya12rus/vkvideo_gui_bot/wiki",
    },
)
