#! /usr/bin/python
#
# This script clones each project from GIT


import subprocess
import os
projects = ['va-ochre',
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

#Developers, set this according to your remote name - 'origin' is the git default, but with multiple remotes, the commented out convention below may work better...
remoteOne = 'origin'
#remoteOne = 'GH-A'
#remoteTwo = 'CN'

gitHubURL = 'https://github.com/Apelon-VA/'

for project in projects:
        if os.path.isdir(os.getcwd() + project)== False:
                print(os.getcwd() + project + " does not exist")
                thisProjectUrl = gitHubURL + project + '.git'
                print("==================================")
                print("Cloning Latest From " + project)
                git("clone", thisProjectUrl)
                print("==================================")
                print("");
        else:
                print(project + " already exists in " + os.getcwd())
