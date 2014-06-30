'''
Created on Apr 13, 2014

@author: henry

follow http://sharats.me/the-ever-useful-and-neat-subprocess-module.html#a-simple-usage
'''

import subprocess

#ls_output=subprocess.check_output(['ls'])
#ls_output = subprocess.check_output(['ls'])


subprocess.Popen('echo "Hello world!"', shell=True)




if __name__ == '__main__':
	pass