# adstxt-crawler
ads.txt crawler for transparency of inventory for publishers and advertisers

# Installation for Ubuntu/Debian

- `sudo apt-get install git`
- `git clone https://github.com/kaustubhd93/adstxt-crawler.git`
- `sudo apt-get install python-pip python-dev build-essential`
- `pip install virtualenv`
- `virtualenv --verbose /path/to/your/virtualenv`
- `source /path/to/your/virtualenv/bin/activate`
- `cd adstxt-crawler`
- `pip install -r requirements.txt`

# Usage
NOTE: List of domains should be written separately each on a new line.
domain1.xyz  
domain2.xyz  
www.domain3.xyz  

- `./crawl.sh /path/to/listofdomainfile`

### CSV Download path : adstxt-crawler/adstxt/csv
