from setuptools import setup, find_packages

setup(
    name="jarvis-ai",  # The name of your package
    version="0.1",  # Package version
    packages=find_packages(),  # Automatically finds all packages
    install_requires=[],  # You can list dependencies here, like 'requests' or 'numpy'
    author="Your Name",  # Your name
    author_email="your.email@example.com",  # Your email
    description="A Python assistant that greets and tells the time",  # A short description of the package
    long_description=open("README.md").read(),  # Long description from the README file
    long_description_content_type="text/markdown",  # Type of the long description (markdown)
    url="https://github.com/yourusername/jarvis",  # Your GitHub repo or project URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
