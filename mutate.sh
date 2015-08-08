#!/bin/bash

#run $1 file, $2 number iterations
echo "  " > tmp.txt
cat $1 > tmp.txt
len="$(wc -c $1 | awk '{print $1}')"

for i in `seq 1 $2`;
do 
    python test.py tmp.txt $len > tmp$i.txt
    cat tmp$i.txt > tmp.txt
done

final="$(echo $1 | sed  's/\./_final./g')"

cat tmp$2.txt > $final
rm tmp*
