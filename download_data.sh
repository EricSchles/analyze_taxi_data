cat data.txt | xargs -n 1 -P 4 wget -c -P data/
