#! /usr/bin/python
#
# Build the entire ISAAC Project
#
#
#

import subprocess
import os
import sys

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


args = ['-e', 'clean']

def mvn(*args):
	print("Running " )
	print(args)
	print(" in " + os.getcwd())
	mvnLocation = "C:\\Program Files\\Maven\\bin\\mvn.bat"
	return print("Output: " + subprocess.check_call([mvnLocation] + list(args)))

for project in projects:
        if os.path.isdir(os.getcwd() + project)== False:
                cwd = os.getcwd()
                print("In: " + cwd + " Entering project " + project)
                print("Enviorment: " + os.environ['JAVA_HOME'])
                os.chdir(project)       
                        
                if project == 'va-expression-service' or project == 'va-isaac-gui-pa':
                        args.extend(['package'])
                else:
                        args.extend(['install'])

                if(len(sys.argv) > 1):
                        if(str(sys.argv[1]) == 'skipTest'):
                                args.extend(['-DskipTests'])
                print ("Build Argument")
                print (args)

                #This fails the build, if it results in a non-0 exit status
                mvn(args)
                
                os.chdir(os.pardir)
        else:
                 print(project + " folder does not exists in " + os.getcwd())
