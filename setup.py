# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'README.md')

setup(
    name="siaw",
    version="0.0.1",
    packages=find_packages(),
    description='Say the same sentence in another way.',
    long_description=open(filepath, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Jack Zhang',
    author_email='snail.zhang@outlook.com',
    url='https://www.zhangjack.com',
    license='MIT',
    install_requires=['jieba>=0.42.1', 'paddlepaddle-tiny==1.6.1', 'pypinyin>=0.37.0'],
    python_requires='>=3',
    package_data={'': ['*.txt']},
    data_files=[filepath],
)
