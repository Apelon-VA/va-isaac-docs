#! /usr/bin/python
#
# Various git commands that Dan uses to fetch all projects from all remotes

# To use this script, you need to have your remote's named "CN" and "GH-A"
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
	return subprocess.check_call(['mvn'] + list(args))

for project in projects:
	os.chdir(project)
	print("Cleaning " + project)
	mvn("clean")
	os.chdir("..")