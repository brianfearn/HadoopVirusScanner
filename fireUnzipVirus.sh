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
