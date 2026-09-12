#!/bin/bash
mkdir backup_check
curl -o holmes.txt https://www.gutenberg.org/cache/epub/1661/pg1661.txt
mv holmes.txt backup_check/holmes.txt
echo "Downloaded and moved holmes.txt to backup_check directory."