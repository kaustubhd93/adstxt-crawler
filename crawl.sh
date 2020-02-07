#!/bin/bash
cd adstxt && scrapy crawl -a fileName=$1 adstxt 
