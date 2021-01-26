import subprocess
import os
vers=''
def getpctype():
	import platform
	return platform.system()

def create_dirs():
	path = os.getcwd()
	projectfolder = path + '/gp8'
	os.mkdir(projectfolder)
	templatesfolder = path + '/gp8/templates'
	os.mkdir(templatesfolder)
	envfolder = path + '/gp8/env'
	os.mkdir(envfolder)

def runp(vers):
	import subprocess
	bashCommand = "cd gp8"
	output = subprocess.check_output(['bash','-c', bashCommand])
	bashCommand2 = "pip install flask"
	output = subprocess.check_output(['bash','-c', bashCommand2])
	bashCommand3 = "export FLASK_ENV=development"
	output = subprocess.check_output(['bash','-c', bashCommand3])
	bashCommand4 = "export FLASK_APP=main.py"
	output = subprocess.check_output(['bash','-c', bashCommand4])
	bashCommand5 = "flask run"
	output = subprocess.check_output(['bash','-c', bashCommand5])

def main ():
	getpctype()
	create_dirs()
	runp(vers)

main()
