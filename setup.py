from setuptools import setup, find_packages

setup(
    name="JARVIS",  # Name of your package
    version="0.1.0",  # Current version
    packages=find_packages(),  # This auto-discovers all packages in your project
    install_requires=[],  # Your project's dependencies
    description="A Python-based assistant",  # A brief description of your project
    author="Nipun Mahajan",  # Your name
    author_email="your.email@example.com",  # Your contact email
    url="https://github.com/yourusername/jarvis",  # Your project’s URL (replace with your actual URL)
    license="MIT",  # Linking the MIT License
    long_description=open('README.md').read(),  # Optional: This includes the contents of your README file
    long_description_content_type="text/markdown",  # Ensures PyPI knows it's markdown
    classifiers=[  # These help categorize your package on PyPI
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
license='MIT'
