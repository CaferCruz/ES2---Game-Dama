#!/bin/bash
DIVISOR="=================================================="
echo $DIVISOR
sudo chmod +x main.py
sudo dos2unix main.py
sed -i -e 's/C:\\Python27\\python/\/usr\/bin\/python/g' main.py  > test.txt
sed -i "2i print \"Content-type: text\/html \\\n\\\n \" " main.py
echo $DIVISOR
