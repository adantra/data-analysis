from setuptools import setup, find_packages

setup(
	name='data-analysis',
	version='0.0.1',
	url='https://github.com/adantra/data-analysis',
	license='BSD',
	author='Adolfo Rodriguez',
	packages=find_packages(),
	install_requires=['pandas',
			  'sqlalchemy',
                          'nltk','numpy','jupyter',
                          'python-twitter','PyQt5'],
	entry_points={},
	extras_require={'dev':['flake8']},
	)
