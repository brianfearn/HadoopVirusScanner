from path import path
import pprint

virus_location = '/home/tetsutech/Downloads/virus-samples'
output_dir = '/home/tetsutech/Downloads/'
virus_types = {}

d = path(virus_location)
o = path(output_dir)

files = d.walkfiles()

total_count = 237540
total_size = '63.7GB'

for f in files:
	temp_string = f.name
	split_name = temp_string.split('.')
	virus_type = split_name[0]
	virus_types[virus_type] = virus_types.get(virus_type, 0) + 1 

pp = pprint.PrettyPrinter()
pp.pprint(virus_types)



