#! /usr/bin/python
#
# Python script to go to each ISAAC project folder and execute a maven clean
#
#
#

import subprocess
import os

#

projects = ['va-isaac-parent',
			'va-ochre',
			'va-isaac-metadata',
			'va-isaac-mojo',
			'va-newtons-cradle',
			'va-logic',
			'va-query-service',
			'va-solor-goods',
			'va-isaac-gui',
			'va-isaac-gui-pa',
			'va-expression-service']

shellVar=False

if (os.name == 'nt'):
	shellVar=True

def mvn(*args):
	return subprocess.check_call(['mvn'] + list(args), shell=shellVar)

for project in projects:
	if os.path.isdir(os.getcwd() + os.sep + project):
		os.chdir(project)
		print("Cleaning " + project)
		mvn("clean")
		os.chdir("..")
	else:
		print(project + " does not exist!")