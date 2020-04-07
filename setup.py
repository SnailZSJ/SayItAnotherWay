# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="siaw",
    version="0.0.2",
    packages=find_packages(),
    description='Say the same sentence in another way.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Jack Zhang',
    author_email='snail.zhang@outlook.com',
    url='https://github.com/SnailZSJ/SayItAnotherWay',
    license='MIT',
    install_requires=['jieba>=0.42.1', 'paddlepaddle-tiny==1.6.1', 'pypinyin>=0.37.0'],
    python_requires='>=3',
    package_data={'': ['*.txt']},
    data_files=['README.md'],
)
