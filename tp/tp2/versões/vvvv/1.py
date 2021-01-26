import subprocess
bashCommand = "cd gp8"
output = subprocess.check_output(['bash','-c', bashCommand])
bashCommand2 = "pip install flask"
output = subprocess.check_output(['bash','-c', bashCommand2])
bashCommand3 = "export FLASK_ENV=main.py"
output = subprocess.check_output(['bash','-c', bashCommand3])
bashCommand4 = "flask run"
output = subprocess.check_output(['bash','-c', bashCommand4])
