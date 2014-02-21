for name in *.zip; do
    unzip -P infected $name;
    name="${name%.*}"
    mv malware.exe $name.exe;
    xxd $name.exe $name.exe.hexdump;
    echo "Created $name.exe and $name.hexdump"
done;
