from path import path
import binascii
import os
import shutil



os.chdir('./../data/virus/')
virus_loc = os.getcwd()
os.chdir('./../normal/')
normal_loc = os.getcwd()
os.chdir('./../')

if os.path.exists(os.getcwd() + '/output/'):
	shutil.rmtree(os.getcwd() + '/output/')
	os.mkdir(os.getcwd() + '/output/')
else:
	os.mkdir(os.getcwd() + '/output/')
	os.chdir('./output/')
	print os.getcwd()

ngram_buffer = []

v = path(virus_loc)
v_files = v.walkfiles()

n = path(normal_loc)
n_files = n.walkfiles()

for f in v_files:
	
	with open(f, 'rb') as f2:
		
		output_name = f.name

		while 1:
			byte = f2.read(1)
			if not byte:
				break
			if len(ngram_buffer) == 7:
				#write out 7 byte feature
				print ''.join(ngram_buffer)
				ngram_buffer.pop(0)
				ngram_buffer.append(binascii.hexlify(byte))
			else:
				ngram_buffer.append(binascii.hexlify(byte))



		



