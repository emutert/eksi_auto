
#!/usr/bin/env python3
# script copies geckodriver 

dest=$(echo $(which python) | sed 's/python//')

#echo $dest
cp ./geckodriver/geckodriver $dest

chk=$(ls ${dest}geckodriver | wc -l)

if [ $chk -ge 1 ]
then 
    echo "geckodriver copied to" $dest
else 
    echo "Error : could not copied"
fi



