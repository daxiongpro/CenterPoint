import os
from setuptools import find_packages, setup


def readme():
    try:
        with open("README.md", encoding="utf-8") as f:
            content = f.read()
        return content
    except:
        return "No description"


if __name__ == "__main__":
    setup(
        name="st-centerpoint",
        version="1.0",
        description="centerpoint det3d",
        long_description=readme(),
        author="daxiongpro",
        author_email="910660298@qq.com",
        keywords="computer vision, 3d object detection",
        url="https://github.com/daxiongpro/centerpoint",
        packages=find_packages(exclude=("configs", "tools", "demo")),
        license="Apache License 2.0",
        setup_requires=["pytest-runner", "cython", "numpy"],
        zip_safe=False,
    )
