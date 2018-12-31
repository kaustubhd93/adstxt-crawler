# WIP
import sys
import os
import urllib2
import re
import datetime
import copy_reg
import pickle
from multiprocessing import Process,Pool,Manager
from helper import HelperFunctions

hlp = HelperFunctions()
manager = Manager()
unCrawlable = manager.list()

class AdsTxt():

    def get_ads_txt(self,domain):
        startTime = datetime.datetime.utcnow()
        hlp.py_logger("Started crawling for domain : " + domain)
        try:
            request = urllib2.Request("https://{}/ads.txt".format(domain))
            request.add_header('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0')
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            hlp.py_logger("Domain {} cannot be crawled. Skipping as something went wrong {}".format(domain,str(e)))
            return None
        contentType = response.headers.getheader('Content-Type')
        if "html" in contentType:
            hlp.py_logger("Domain {} cannot be crawled. Skipping as html content found".format(domain))
            return None
        content = response.readlines()
        inventoryDetails = []
        for line in content:
            if "ads.txt" not in line.lower():
                if re.search(r'direct',line.lower(),re.M|re.I):
                    relation = "DIRECT"
                elif re.search(r'direct\|reseller',line.lower(),re.M|re.I):
                    relation = "DIRECT|RESELLER"
                elif re.search(r'reseller',line.lower(),re.M|re.I):
                    relation = "RESELLER"
                else:
                    relation = "undefined"
                partnerDetails = line.strip("\n\r").split(",")
                if len(partnerDetails) > 1:
                    if not re.search(r'(direct)|(reseller)',partnerDetails[1].lower(),re.M|re.I):
                        pubId = partnerDetails[1].strip()
                    else:
                        pubId = None
                    inventoryDetails.append({"partner": partnerDetails[0],
                                             "pubId" : pubId,
                                             "relation" : relation})
                        
               
        adstxt = {"domain" : domain,
                  "adstxt" : inventoryDetails}
        hlp.py_logger("Finished crawling for domain : " + domain)
        endTime = datetime.datetime.utcnow()
        hlp.py_logger("Time lapsed in crawling : {}".format(hlp.cal_diff(startTime, endTime)))
        hlp.write_to_csv(adstxt["adstxt"],fileName=domain,fieldNames=["partner","pubId","relation"])
        #return adstxt

if __name__ == "__main__":
     # File with list of domains
     domainFileName = sys.argv[1]
     
     # Take all domains.
     fObj = open(domainFileName, "r+")
     domainList = fObj.readlines()
     fObj.close()

     ads = AdsTxt()
     domainList = map(lambda x: x.strip("\n"), domainList)
     # Make equal sized chunks of list
     domainBatch = hlp.split_list_into_chunks(domainList,20)
     for batch in domainBatch:
         jobs = []
         for domainName in batch:
             worker = Process(target=ads.get_ads_txt, args=(domainName,))
     
     #for domain in domainList:
     #    domainAdsTxt = ads.get_ads_txt(domain)
     #    if domainAdsTxt:
     #        csvFileName = domainAdsTxt["domain"]
     #        hlp.write_to_csv(domainAdsTxt["adstxt"],fileName=csvFileName,fieldNames=["partner","pubId","relation"])
     #    else:
     #        unCrawlable.append(domain)
     #if unCrawlable:
     #   hlp.py_logger("List of domains that could not be crawled : {}.".format(unCrawlable))
     #pool = Pool(processes=20)
     #pool.apply_async(ads.get_ads_txt(),domainList)
     
     
