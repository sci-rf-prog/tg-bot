import os

CURR_PATH = os.path.dirname(__file__) + '/../static/'

with open(os.path.join(CURR_PATH, 'prog.txt'), 'r') as txt_file:
	prog_info = txt_file.read()
with open(os.path.join(CURR_PATH, 'razv.txt'), 'r') as txt_file:
	razv_info = txt_file.read()
with open(os.path.join(CURR_PATH, 'rob.txt'), 'r') as txt_file:
	robot_info = txt_file.read()
with open(os.path.join(CURR_PATH, 'scipo.txt'), 'r') as txt_file:
	scipo_info = txt_file.read()
with open(os.path.join(CURR_PATH, 'inf.txt'), 'r') as txt_file:
	inf_info = txt_file.read()