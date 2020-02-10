#!/bin/bash
cd adstxt
if [ ! -d "csv" ]
then
    echo "Adding directory csv in `pwd`"
    mkdir -p csv
    echo "Added directory successfully."
fi
scrapy crawl -a fileName=$1 adstxt
echo "All scraped csv files are in `pwd`/csv"
