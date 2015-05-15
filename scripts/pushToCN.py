#! /usr/bin/python
#
# Various git commands that Dan uses to fetch from both CN and GH-A, and then push commits from GH-A to CN

# To use this script, you need to have your remote's named "CN" and "GH-A" (or update the variables below)
#

import subprocess

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

#Developers, set this according to your remote names - the names below are simply Dan's default convention
remoteMaster = 'GH-A'
remoteSlave = 'CN'

for project in projects:
	print("==================================")
	print("Fetching Latest from " + project)
	git("-C", project, "fetch", remoteMaster)
	git("-C", project, "fetch", remoteSlave)
	
	print("Pushing develop branch from " + remoteMaster + " to " + remoteSlave)
	git("-C", project, "push", remoteSlave, remoteMaster + "/develop:develop")

	print("Pushing master branch from " + remoteMaster + " to " + remoteSlave)
	git("-C", project, "push", remoteSlave, remoteMaster + "/master:master")

	print("Pushing Tags to " + remoteSlave)
	git("-C", project, "push", remoteSlave, "--tags")
	print("==================================")
	print("");