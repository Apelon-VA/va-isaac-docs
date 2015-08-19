#! /usr/bin/python
#
# Merge (synchronize) the ISAAC-Developers repositories  with their forked upstream counterparts on Apelon-VA account


import subprocess
import os
import argparse
parser = argparse.ArgumentParser(description='Merge ISAAC-Developers GitHub Account with the Forked repositories on the Apelon-VA GitHub account')
parser.add_argument('-s', '--branch', type=string, default=develop,
					help='The default branch is develop, but you can specify any branch here')
# TODO: Finish implementing CLI Arguments for the branch

projects = ['va-isaac-docs',
			'va-isaac-parent',
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

if (os.name == 'nt'):
	shellVar=True
			
def git(*args):
	print("Arguments: ")
	print(list(args))
	return subprocess.check_call(['git'] + list(args), shell=shellVar)

gitHubURL = 'https://github.com/ISAAC-Developers/'
branch = 'develop'

forkedUrl = 'https://github.com/Apelon-VA/'
forkedBranch = 'develop'

for project in projects:
		if os.path.isdir(os.getcwd() + os.sep + project):
				print("In: " + os.getcwd() + " Entering project " + project)
				os.chdir(project)
				
				thisProjectUrl = gitHubURL + project + '.git'
				thisforkedProjectUrl = forkedUrl + project + '.git'
				
				print("")
				print("==================================")
				print("Adding Remote " + thisforkedProjectUrl + " branch " + forkedBranch)
				
				tmpBranch = ''
				if project == 'va-isaac-docs':
					tmpBranch = 'master'
					tmpforkedBranch = 'master'
				else:
					tmpBranch = branch
					tmpforkedBranch = forkedBranch
					
				git("remote", "-v")
				git("remote", "add", "upstream", thisforkedProjectUrl)
				git("remote", "-v")
				git("fetch", "upstream")
				git("checkout", branch)
				git("merge", "upstream/" + forkedBranch)
				#TODO: Verify that there are no changes before merging
				print("==================================")
				
		else:
				print(project + " does not exist in " + os.getcwd())
