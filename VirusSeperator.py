from path import path

virus_location = '/home/tetsutech/Downloads/viruses-2010-05-18'
output = '/home/tetsutech/Downloads/virus-samples'
output_file_count = 0
total_file_count = 0
directory_counter = 1



d = path(virus_location)
e = path(output)

if not e.exists():
	e.mkdir()

files = d.files("*Win32*")
length = len(files)

output_path = path(output+'/'+str(directory_counter))

for f in files:
	
	
	if not output_path.exists():
		output_path.mkdir()	

	f.copy(output_path)
	output_file_count += 1
	total_file_count += 1

	if output_file_count == 10000:
		directory_counter += 1
		output_file_count = 0
		output_path = path(output+'/'+str(directory_counter))

				
	if total_file_count % 10000 == 0:
		print total_file_count

