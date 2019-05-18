import sys
import scrapy
sys.path.append('../')
from adstxtcrawler import get_ads_txt

domainDetails = sys.argv[1]

class AdstxtSpider(scrapy.Spider):
    name = "adstxt"

    def start_requests(self):
        #fObj = open("/home/kaustubh/Workspace/adstxt-crawler/sample", "r+")
        fObj = open(self.domainDetails, "r+")
        domainList = fObj.readlines()
        fObj.close()
        domainList = map(lambda x: x.strip("\n"), domainList)
        for domain in domainList:
            yield scrapy.Request(url="http://{}/ads.txt".format(domain), callback=self.parse)

    def parse(self, response):
        #print dir(response)
        domain = response.url.split("/")[-2]
        # filename = 'adstxt-%s.txt' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        get_ads_txt(domain, response.body, True)
        self.log('Saved file *********************************************')
