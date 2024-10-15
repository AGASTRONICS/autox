from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A self-hosted trading bot'
LONG_DESCRIPTION = (f'''
    A self-hosted trading bot for automated trading.
''')

setup(
    name='autox',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Abdulsamad .O. ABDULGANIYU',
    author_email='agastronics@gmail.com',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'autox=autox:main',
        ],
    },
    keywords=['python', 'autox', 'trading', 'bot'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
