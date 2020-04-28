import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="suser_engelle", # Replace with your own username
    version="0.0.1",
    author="emutert",
    description="enty favlayan tüm suserleri engeller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emutert/eksi_auto",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    py_modules=['cli','eksi_engelle'],
    install_requires=[
        'selenium',
        'prompt_toolkit',
        
    ],
     entry_points='''
        [console_scripts]
        suser_engelle = cli:main
    ''',
)