## adstxt-crawler
ads.txt is an IAB-approved text file that aims to prevent unauthorized inventory sales. Publishers drop a text file on their web servers that lists all of the companies that are authorized to sell the publisher's inventory. Similarly, programmatic platforms also integrate ads.txt files to confirm which publishers’ inventory they are authorized to sell. This allows buyers to check the validity of the inventory they purchase.
[Tell me more about this](https://github.com/kaustubhd93/adstxt-crawler/wiki/Ads.txt-concepts)  

## Installation steps for Ubuntu/Debian

- `sudo apt-get install git`
- `git clone https://github.com/kaustubhd93/adstxt-crawler.git`
- `sudo apt-get install python-pip python-dev build-essential`
- `sudo pip install virtualenv`
- `virtualenv /path/to/your/virtualenv`
- `source /path/to/your/virtualenv/bin/activate`
- `cd adstxt-crawler`
- `pip install -r requirements.txt`

## Installation steps for CentOs/Fedora

- `sudo yum update` (if os is newly installed.)
- `sudo yum install epel-release`
- `sudo yum install git`
- `git clone https://github.com/kaustubhd93/adstxt-crawler.git`
- `sudo yum install gcc* python-devel python-pip`
- `sudo pip install -U pip`
- `sudo pip install virtualenv`
- `virtualenv /path/to/your/virtualenv`
    - Run this if virtualenv threw an import error `sudo pip install -U zipp configparser`. Ignore this if virtualenv succeeded.
- `source /path/to/your/virtualenv/bin/activate`
- `cd adstxt-crawler`
- `pip install -r requirements.txt`


## Usage
NOTE: List of domains should be written separately each on a new line.  
```
domain1.xyz  
domain2.xyz  
www.domain3.xyz  
```
### Crawl ads.txt by running below command

- `./crawl.sh /path/to/listofdomainfile`

#### CSV Download path : adstxt-crawler/adstxt/csv

## Running Docker already ? Then, no need to setup all those things mentioned above.
> If you are not running docker and want to use it. Check this installation guide for docker : https://docs.docker.com/get-docker/

### Please follow these steps in the exact order

- `docker pull kaustubhdesai/adstxtcrawler:0.1`
- `docker volume create adstxtcrawler`
- `docker run -id --name adstxtcrawler --mount source=adstxtcrawler,target=/app/adstxt/csv adstxtcrawler:0.1`
- `docker cp /path/to/file/with/domains/filename adstxtcrawler:/app/filename`
- `docker exec adstxtcrawler bash -c "./crawl.sh /app/filename"`
- Once above command has exited properly, run this command to check downloaded csv files.
- `cd /var/lib/docker/volumes/adstxtcrawler/_data`

