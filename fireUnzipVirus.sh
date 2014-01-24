for Z_FILE in *.zip; do unzip -P infected $Z_FILE; done;
set count = 0;
for Z_FILE in *.pl; do xxd $Z_FILE $Z_FILE.hexdump; set count += 1; echo count; done;
