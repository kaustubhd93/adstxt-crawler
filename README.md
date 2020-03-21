# adstxt-crawler
ads.txt crawler for transparency of inventory for publishers and advertisers.  
[Know more](https://github.com/kaustubhd93/adstxt-crawler/wiki/Ads.txt-concepts)  

# Installation for Ubuntu/Debian
> Please note this code only works on Python3
- `sudo apt-get install git`
- `git clone https://github.com/kaustubhd93/adstxt-crawler.git`
- `sudo apt install python3-venv python3.5-dev build-essential`
- `python3.5 -v -m venv /path/to/your/virtualenv`
- `source /path/to/your/virtualenv/bin/activate`
- `cd adstxt-crawler`
- `pip install -U pip`
- `pip install -r requirements.txt`

# Usage
NOTE: List of domains should be written separately each on a new line.  
```
domain1.xyz  
domain2.xyz  
www.domain3.xyz  
```

- `./crawl.sh /path/to/listofdomainfile`

### CSV Download path : adstxt-crawler/adstxt/csv
