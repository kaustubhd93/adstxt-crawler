# WIP
import sys
import os
import urllib2
import re
import datetime
import json
from multiprocessing import Process,Pool,Manager
from helper import HelperFunctions

hlp = HelperFunctions()
manager = Manager()
unCrawlable = manager.list()

def get_content(domain):
    hlp.py_logger("Started crawling for domain : " + domain)
    try:
        request = urllib2.Request("https://{}/ads.txt".format(domain))
        request.add_header('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0')
        response = urllib2.urlopen(request, timeout=3)
    except urllib2.URLError as e:
        hlp.py_logger("Trying with http for domain {}".format(domain))
        try:
            request = urllib2.Request("http://{}/ads.txt".format(domain))
            request.add_header('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0')
            response = urllib2.urlopen(request, timeout=3)
        except Exception as e:
            hlp.py_logger("Domain {} cannot be crawled. Skipping as something went wrong {}".format(domain,str(e)))
            unCrawlable.append(domain)
            return None
    except Exception as e:
        hlp.py_logger("Domain {} cannot be crawled. Skipping as something went wrong {}".format(domain,str(e)))
        unCrawlable.append(domain)
        return None
    contentType = response.headers.getheader('Content-Type')
    if contentType:
        if "html" in contentType:
            hlp.py_logger("Domain {} cannot be crawled. Skipping as html content found".format(domain))
            unCrawlable.append(domain)
            return None
    else:
        hlp.py_logger("Content type is blank for domain {}. Skipping this for now".format(domain))
        unCrawlable.append(domain)
        return None
    try:
        content = response.readlines()
        return content
    except Exception as e:
        hlp.py_logger("Something went wrong while read operation {} for domain {}".format(str(e),domain))
        return None

def get_ads_txt(domain):
    content = get_content(domain)
    if content:
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
                    if len(partnerDetails) >= 4:
                        if "#" in partnerDetails[3]:
                            tagEle = partnerDetails[3].split("#")
                            tagId = tagEle[0].strip()
                        else:
                            tagId = partnerDetails[3].strip()
                    else:
                        tagId = None
                    inventoryDetails.append({"partner": partnerDetails[0],
                                             "pubId" : pubId,
                                             "relation" : relation,
                                             "tagId" : tagId})
                        
               
        adstxt = {"domain" : domain,
                  "adstxt" : inventoryDetails}
        hlp.py_logger("Finished crawling for domain : " + domain)
        #endTime = datetime.datetime.utcnow()
        #hlp.py_logger("Time lapsed in crawling : {}".format(hlp.cal_diff(startTime, endTime)))
        #fObj = open("json/crawledDomains.json","a+")
        #try:
        #    fObj.write(json.dumps(adstxt)+"\n")
        #except Exception as e:
        #    hlp.py_logger("Somthing went wrong while json encoding for domain {} - {}.".format(domain,str(e)))
        #    return None
        #fObj.close()
        hlp.write_to_csv(adstxt["adstxt"],fileName=domain,fieldNames=["partner","pubId","relation","tagId"])
        #return adstxt

if __name__ == "__main__":
    # File with list of domains
    domainFileName = sys.argv[1]
    
    # Take all domains.
    fObj = open(domainFileName, "r+")
    domainList = fObj.readlines()
    fObj.close()

    #ads = AdsTxt()
    domainList = map(lambda x: x.strip("\n"), domainList)
    #for domain in domainList:
    #    get_ads_txt(domain)
    pool = Pool(processes=30)
    pool.map(get_ads_txt, domainList)
    hlp.py_logger("List of domains that could not be crawled : {}.".format(unCrawlable))
     
