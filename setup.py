import os
from setuptools import setup

required = [
    'numpy',
    'PIL',
    'matplotlib',
    'sklearn',
    'cv2',
    'tkinter'
]

with open("README.md", "r") as fh:
    long_description = fh.read() 

setup(
    name='polygon_crop',
    version='0.0.1',
    description = 'An image processing package which supports interactive cropping function',
    packages=[
        'polygon_crop'
        ],
    license='MIT',
    author_email = 'jchiang1225@gmail.com',
    url = 'https://github.com/chiang9/polygon_crop',
    install_requires = required,
    author = 'Kuan-Yu Chiang',
    long_description= long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
  ],
)