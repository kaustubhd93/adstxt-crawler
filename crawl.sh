#!/bin/bash
cd adstxt
if [ ! -d "csv" ]
then
    echo "Adding directory csv in `pwd`"
    mkdir -p csv
    echo "Added directory successfully."
fi
scrapy crawl -a fileName=$1 adstxt
lastStatusCode=$(echo $?)
if [ $lastStatusCode -ne 0 ]
then
    echo "******************************************************************************"
    echo "Something went wrong here."
    echo "******************************************************************************"
else
    echo "******************************************************************************"
    echo "All scraped csv files are in `pwd`/csv"
    echo "******************************************************************************"
    echo "If there were urls that could not be scraped, refer log file: `pwd`/scrapy.log"
    echo "******************************************************************************"
fi
