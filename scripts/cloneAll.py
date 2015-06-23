#! /usr/bin/python
#
# This script clones each project from GIT


import subprocess
import os
projects = ['va-isaac-docs',
			'va-isaac-parent',
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

def git(*args):
		return subprocess.check_call(['git'] + list(args))

gitHubURL = 'https://github.com/Apelon-VA/'
branch = 'develop'

for project in projects:
		if os.path.isdir(os.getcwd() + os.sep + project)== False:
				print(os.getcwd() + os.sep + project + " does not exist")
				thisProjectUrl = gitHubURL + project + '.git'
				print("==================================")
				print("Cloning Latest From " + project)
				
				tmpBranch = ''
				if project == 'va-isaac-docs':
					tmpBranch = 'master'
				else:
					tmpBranch = branch
				
				git("clone", "--branch", tmpBranch, thisProjectUrl)
				print("==================================")
				print("");
		else:
				print(project + " already exists in " + os.getcwd())
