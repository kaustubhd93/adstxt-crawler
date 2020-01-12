import sys
import scrapy
sys.path.append('../')
from adstxtcrawler import get_ads_txt

class AdstxtSpider(scrapy.Spider):
    name = "adstxt"

    def start_requests(self, fileName=""):
        fObj = open(self.fileName, "r+")
        domainList = fObj.readlines()
        fObj.close()
        domainList = map(lambda x: x.strip("\n"), domainList)
        for domain in domainList:
            yield scrapy.Request(url="http://{}/ads.txt".format(domain), callback=self.parse)

    def parse(self, response):
        domain = response.url.split("/")[-2]
        get_ads_txt(domain, response.body, True)
        self.log('Saved file *********************************************')
