#! /usr/bin/python
#
# Python script to go to each ISAAC project folder and execute a maven clean
#

import subprocess
import os

projects = ['va-isaac-parent',
			'va-ochre',
			'va-isaac-metadata', 
			'va-isaac-mojo', 
			'va-newtons-cradle', 
			'va-logic', 
			'va-query-service', 
			'va-isaac-gui', 
			'va-solor-goods', 
			'va-expression-service', 
			'va-isaac-gui-pa']

def mvn(*args):
	return subprocess.check_call(['mvn'] + list(args), Shell=True)

for project in projects:
	if os.path.isdir(os.getcwd() + os.sep + project):
		os.chdir(project)
		print("Cleaning " + project)
		mvn("clean")
		os.chdir("..")