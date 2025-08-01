from setuptools import setup

setup(
    name="task-tracker",
    version="1.0.0",
    description="A CLI application to manage tasks.",
    author="Yoendi",
    author_email="yoendigy1408@gmail.com",
    url="https://github.com/YoendiGarcia/Task-Tracker-CLI",
    py_modules=["task-tracker"],
    entry_points={
        "console_scripts": [
            "task-tracker=task-tracker:main",
        ],
    },
    tests_require=[
        "pytest",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)