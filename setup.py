import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlierpack-NG",
    version="0.0.5",
    author="Nikhil Gupta",
    author_email="ngupta_be17@thapar.edu",
    description="Outlier removal using pandas",
	url='https://github.com/CachingNik/niklib',
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	scripts=['bin/outcli'],
	keywords = ['CLI', 'OUTLIER', 'Data', 'outlier removal'], 
	python_requires='>=2.7', 
)
