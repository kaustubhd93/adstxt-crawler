# WIP
import sys
import os
import urllib2
import re
import datetime
from helper import HelperFunctions

hlp = HelperFunctions()

class AdsTxt():

    def get_ads_txt(self,domain):
        startTime = datetime.datetime.utcnow()
        hlp.py_logger("Started crawling for domain : " + domain)
        response = urllib2.urlopen("https://{}/ads.txt".format(domain))
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
        return adstxt

if __name__ == "__main__":
     # File with list of domains
     domainFileName = sys.argv[1]
     
     # Take all domains.
     fObj = open(domainFileName, "r+")
     domainList = fObj.readlines()
     fObj.close()

     ads = AdsTxt()
     
     for domain in domainList:
         domainAdsTxt = ads.get_ads_txt(domain.strip("\n"))
         csvFileName = domainAdsTxt["domain"]
         hlp.write_to_csv(domainAdsTxt["adstxt"],fileName=csvFileName,fieldNames=["partner","pubId","relation"])
