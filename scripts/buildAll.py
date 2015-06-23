#! /usr/bin/python
#
# Build the entire ISAAC Project
#
#
#

import subprocess
import os
import sys

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


defaultArgs = ['-e', 'clean']

def mvn(args):
    return subprocess.check_call(['mvn'] + args, Shell=True)


for project in projects:
	cwd = os.getcwd()
	print("In: " + cwd + " Entering project " + project)
	os.chdir(project)

	args = defaultArgs[:]
	if project == 'va-expression-service' or project == 'va-isaac-gui-pa':
		args.extend(['package'])
	else:
		args.extend(['install'])

	print ("Build Argument")
	print (args)

	#This fails the build, if it results in a non-0 exit status
	mvn(args)
	
	os.chdir(os.pardir)

