from setuptools import setup, find_packages

with open('requirements.txt') as f:
	requirements = f.readlines()

long_description = 'A Command Line Tool made to manage dependency versions.'

setup(
		name ='dyteproject',
		version ='1.0.1',
		author ='Prakhar Sharma',
		author_email ='prakharsharma1607@gmail.com',
		url ='https://github.com/dyte-submissions/dyte-vit-2022-PS1607',
		description ='A tool to Maintain & Manage dependencies.',
		long_description = long_description,
		long_description_content_type ="text/markdown",
		license ='MIT',
		packages = find_packages(),
		entry_points ={
			'console_scripts': [
				'dependency = dyteproject.main:main'
			]
		},
		classifiers =(
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		),
		keywords ='Dependency dyte github',
		install_requires = requirements,
		zip_safe = False
)
