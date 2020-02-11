import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlierpack-NG",
    version="0.1.0",
    author="Nikhil Gupta",
    author_email="ngupta_be17@thapar.edu",
    description="Removing outliers from a pandas dataframe",
	url='https://github.com/CachingNik/OutlierPack',
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	entry_points = {
        'console_scripts': ['Outcli=outlib.outcli:main'],
    },
	keywords = ['CLI', 'OUTLIER', 'Data', 'outlier removal'], 
	python_requires='>=2.7', 
)
