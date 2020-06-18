from setuptools import setup, find_packages

setup(
    name="edalogparser",

    use_scm_version={
        "relative_to": __file__,
        "write_to": "edalogparser/version.py",
    },

    description="Parse EDA tool output",

    url="https://github.com/librecores/eda-log-parser",

    author="Stefan Wallentowitz",

    author_email="stefan@fossi-foundation.org",

    classifiers=[
        "Development Status :: 3 - Alpha",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",
    ],

    packages=find_packages(),

    setup_requires=[
        'setuptools_scm',
    ],

    entry_points={
        "console_scripts": [
            "eda-log-parser=edalogparser.main:main",
        ],
    },
)
