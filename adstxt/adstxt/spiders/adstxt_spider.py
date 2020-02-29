import sys
import scrapy

from scrapy import signals
from multiprocessing import Manager
# Importing parsing logic and helper functions.
# NOTE: There is a in built package "parser" that is shipped in Python 3.
from .adstxtparser.parsers import adstxtcrawler
#from .adstxtparser import parsers

manager = Manager()
failedDomains = manager.list()

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
        #parsers.adstxtcrawler.get_ads_txt(domain, response.body)
        self.logger.debug("Saved file for domain {}".format(domain))

    def http_error(self, failure):
        self.logger.error(repr(failure))
        failedDomainUrl = failure.request.url
        print("Could not scrape : {}".format(failedDomainUrl))
        failedDomains.append(failedDomainUrl.split("/")[-2])

    def closed(self, reason):
        # This part is provisional as later on when the UI is built on top of this,
        # The list can be stored in Redis or a sql database.
        if failedDomains:
            print("\nList of domains that could not be scraped : {}\n".format(failedDomains))
        else:
            return None
