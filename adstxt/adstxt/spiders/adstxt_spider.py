import sys
import scrapy

from parser.parsers import adstxtcrawler

class AdstxtSpider(scrapy.Spider):
    name = "adstxt"

    def start_requests(self, fileName=""):
        fObj = open(self.fileName, "r+")
        domainList = fObj.readlines()
        fObj.close()
        domainList = map(lambda x: x.strip("\n"), domainList)
        for domain in domainList:
            yield scrapy.Request(url="http://{}/ads.txt".format(domain),
                                    callback=self.parse,
                                    errback=self.http_error)

    def parse(self, response):
        domain = response.url.split("/")[-2]
        adstxtcrawler.get_ads_txt(domain, response.body)
        self.log("Saved file *********************************************")

    def http_error(self, failure):
        print("Could not scrape : {}".format(failure.request.url))
