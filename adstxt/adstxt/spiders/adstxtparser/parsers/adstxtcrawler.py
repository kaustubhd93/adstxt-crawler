# WIP
import re
from .helper import HelperFunctions

hlp = HelperFunctions()

def get_ads_txt(domain, data):
    content = data.splitlines()
    if content:
        inventoryDetails = []
        csvinventoryDetails = []
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
                    csvinventoryDetails.append({"partner": partnerDetails[0],
                                                 "pubId" : pubId,
                                                 "relation" : relation,
                                                 "tagId" : tagId})

        adstxt = {"domain" : domain,
                "adstxt" : csvinventoryDetails}
        hlp.write_to_csv(adstxt["adstxt"],fileName=domain,fieldNames=["partner","pubId","relation","tagId"])
