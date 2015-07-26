#!/bin/bash

cd ~
mkdir test2014
cd test2014
mkdir sub2014
cd sub2014
touch myfile.txt
mv myfile.txt myfile1.txt

for ((i=1;i<10;i++))
    do
        cp myfile$i.txt myfile$(($i+1)).txt
    done
ls -l

# subl tt.sh
# chmod +x tt.sh
# #!/bin/bash
# ./tt.sh
