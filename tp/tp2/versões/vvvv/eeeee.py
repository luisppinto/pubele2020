import os
vers=''
def getpctype():
	import platform
	vers=platform.system()
	return vers

def create_dirs():
	path = os.getcwd()
	projectfolder = path + '/gp8'
	
	os.mkdir(projectfolder)
	templatesfolder = path + '/gp8/templates'
	os.mkdir(templatesfolder)
	envfolder = path + '/gp8/env'
	
def runp(vers):
        if (vers == 'Windows'):
                def install_env():
                    os.system('cmd /c "cd gp8 & py -3 -m venv env"')

                def openserver():
                    os.system('cmd /k "cd gp8 & env\Scripts\activate & pip install Flask & pip install requests & pip install regex & set FLASK_APP=main.py & flask run"')

        elif (vers =='Linux'):
             os.system("cd gp8")
             os.system("pip install flask")
             os.system("export FLASK_ENV=main.py")
             os.system("flask run")

def main ():
        getpctype()
        create_dirs()
        runp(vers)
main()
