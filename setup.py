from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bountyhunter-pro",
    version="5.0.0",
    author="0r1V4x",
    description="Complete GUI-based bug bounty automation platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0r1V4x/bug-automation",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8+",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "customtkinter>=5.2.0",
        "Pillow>=10.0.0",
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "dnspython>=2.4.0",
        "python-nmap>=0.7.1",
        "pyyaml>=6.0.0",
        "psutil>=5.9.0",
    ],
    entry_points={
        "console_scripts": [
            "bountyhunter=bountyhunter:main",
        ],
    },
    include_package_data=True,
)
