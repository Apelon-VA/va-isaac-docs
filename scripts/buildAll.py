#! /usr/bin/python
#
# Build the entire ISAAC Project

import subprocess
import os
import sys
import argparse
parser = argparse.ArgumentParser(description='Build entire ISAAC Project Suite')
parser.add_argument('-s', '--skipTests', action='store_true',
					help='Skip the Maven Tests by executing the install command with the -DskipTests flag')

projects = ['va-isaac-parent',
			'va-ochre',
			'va-isaac-metadata',
			'va-isaac-mojo',
			'va-newtons-cradle',
			'va-query-service',
			'va-logic',
			'va-solor-goods',
			'va-isaac-gui',
			'va-isaac-gui-pa',
			'va-expression-service']

cliArgs = parser.parse_args()
defaultArgs = ['-e', 'clean']
shellVar=False

if (os.name == 'nt'):
	shellVar=True

def mvn(args):
	return subprocess.check_call(['mvn'] + args, shell=shellVar)


for project in projects:
	cwd = os.getcwd()
	print("In: " + cwd + " Entering project " + project)
	os.chdir(project)

	args = defaultArgs[:]
	if project == 'va-expression-service' or project == 'va-isaac-gui-pa':
		args.extend(['package'])
	else:
		args.extend(['install'])
		
	if cliArgs.skipTests:
		args.extend(['-DskipTests'])

	print ("Build Argument")
	print (args)

	#This fails the build, if it results in a non-0 exit status
	mvn(args)
	
	os.chdir(os.pardir)