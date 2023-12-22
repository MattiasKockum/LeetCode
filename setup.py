from setuptools import setup, find_packages

setup(
    name='leetcode',
    version='0.1',
    author='Mattias',
    description='Some leet code challenges',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'leetcode=leetcode.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GPL',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
