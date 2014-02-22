from path import path
import binascii


virus_loc = '/home/tetsutech/Downloads/virusdata'

ngram_buffer = []

d = path(virus_loc)
files = d.walkfiles()

for f in files:
	with open(f, 'rb') as f2:
		
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



		
