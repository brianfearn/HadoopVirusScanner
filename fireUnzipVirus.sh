<<<<<<< HEAD
set x = 0;
for Z_FILE in *.zip; do
    let x++;
    echo $x;
    echo $Z_FILE;
    unzip -P infected $Z_FILE;
    mv malware.exe $x.exe;
    echo $x.exe;
    xxd $x.exe $x.hexdump;
done;
=======
for Z_FILE in *.zip; do unzip -P infected $Z_FILE; done;
set count = 0;
for Z_FILE in *.pl; do xxd $Z_FILE $Z_FILE.hexdump; set count += 1; echo count; done;
>>>>>>> origin/master
