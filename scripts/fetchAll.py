#! /usr/bin/python
#
# Various git commands that Dan uses to fetch all projects from all remotes

#
#
#

import subprocess


projects = ['va-isaac-docs',
			'va-isaac-parent',
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

def git(*args):
	return subprocess.check_call(['git'] + list(args))

#Developers, set this according to your remote name - 'origin' is the git default, but with multiple remotes, the commented out convention below may work better...
remoteOne = 'origin'
#remoteOne = 'GH-A'
#remoteTwo = 'CN'

for project in projects:
	print("==================================")
	print("Fetching Latest from " + project)
	git("-C", project, "fetch", remoteOne)
#	git("-C", project, "fetch", remoteTwo)
	print("==================================")
	print("");