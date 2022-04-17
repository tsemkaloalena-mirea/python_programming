import setuptools

setuptools.setup(
    name="package_for_task5",
    version="0.1.2",
    author="AlenaTsemkalo",
    author_email="tsemkaloalena@gmail.com",
    description="This is a test package.",
    packages=['task5_package'],
    package_data={'': ['file.json']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
