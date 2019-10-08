TMP_FILE=/tmp/frame.png

convert -pointsize 50 -fill blue -draw 'text 100,200 "Leela Pakanati" ' boris.jpg $TMP_FILE 

sudo fbi -a -noverbose -T 1 $TMP_FILE
