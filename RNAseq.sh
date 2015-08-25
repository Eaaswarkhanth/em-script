# number 1 is search sequence
# number 2 is list of files to search
echo "Enter file list"
read filelist
echo "Enter search term"
read sequence

for filenames in `${filelist}` 
	do grep -i -B 1 ${sequence} ${filenames} | #search for the thingI 
	 grep  ">" | #search for header lines
	 cut -f 1 -d " "| #Only keep sequence name
	 cut -c 2- #get rid of ">"
done
