from setuptools import setup, find_packages

setup(
    name='montecarlo_simulator',
    version='1.0.0',
    packages=find_packages(),  # Automatically finds 'montecarlo_simulator' folder
    install_requires=[
        'numpy',
        'pandas'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A Monte Carlo simulator using Die, Game, and Analyzer classes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/montecarlo_simulator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
