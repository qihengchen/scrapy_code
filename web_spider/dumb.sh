#!/bin/bash

rm -rf output/urlfile.txt
counter=0
while [ $counter -le 79 ]
do
	url="$(python script.py $counter)"
	scrapy crawl amazon_spider -a cat_url=$url --loglevel ERROR
	echo $url
	((counter++))
done



