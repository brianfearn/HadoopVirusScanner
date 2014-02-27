from path import path
import binascii
import os
import shutil



os.chdir('./../data/virus/')
virus_loc = os.getcwd()
#os.chdir('./../normal/')
#normal_loc = os.getcwd()
os.chdir('./../')

if os.path.exists(os.getcwd() + '/output/'):
	shutil.rmtree(os.getcwd() + '/output/')
	os.mkdir(os.getcwd() + '/output/')
else:
	os.mkdir(os.getcwd() + '/output/')
	os.chdir('./output/')
	print os.getcwd()

os.mkdir(os.getcwd() + '/output/virus/')
os.mkdir(os.getcwd() + '/output/normal/')

ngram_buffer = []

v = path(virus_loc)
v_files = v.walkfiles()

#n = path(normal_loc)
#n_files = n.walkfiles()


normal_features = set()

for f in v_files:
	
	with open(f, 'rb') as f2:
		
		output_name = f.name
		with open(os.getcwd() + '/output/virus/' + f.name + '.bif', 'a') as f3:

			virus_features = set()

			while 1:
				byte = f2.read(1)
				if not byte:
					break
				if len(ngram_buffer) == 7:
				#write out 7 byte feature
					feature = (''.join(ngram_buffer))
					if feature not in virus_features:
						virus_features.add(feature)


					#f3.write(feature)
					#f3.write('\n')
					ngram_buffer.pop(0)
					ngram_buffer.append(binascii.hexlify(byte))
				else:
					ngram_buffer.append(binascii.hexlify(byte))

			for vf in virus_features:
				f3.write('+')
				f3.write(vf)
				f3.write('\n')


		



