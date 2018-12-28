import os
import logging
import csv
import time

projectDir = os.getcwd()

class HelperFunctions():

    def py_logger(self, logData, logType='debug', name='crawler', rotate=False):
        logFileName = projectDir + '/logs/' + name + '.log'
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(name)
    
        if logType == 'debug':
            level = logging.DEBUG
        else:
            level = logging.ERROR
    
        handler = logging.FileHandler(logFileName, mode='a')
        handler.setFormatter(formatter)
    
        logger.setLevel(level)
        logger.addHandler(handler)
    
        if logType == 'debug':
            logger.debug(logData)
        else:
            logger.exception(logData)
    
        logger.handlers = []

    def write_to_csv(self, listInfo, fileName, fieldNames=["partner","pubid","relation"], overwrite=False):
        timeFormat = time.strftime("%Y-%m-%d-%H-%M")
        if not overwrite:
            csvFileName = projectDir + "/csv/" + fileName + "-" + timeFormat + ".csv"
        else:
            csvFileName = projectDir + "/csv/" + fileName + ".csv"
        #with open(projectDir + "/csv/" + fileName + timeFormat + ".csv", "w") as fileData:
        with open(csvFileName, "w") as fileData:
            writer = csv.DictWriter(fileData, fieldnames=fieldNames)
            writer.writeheader()
            for info in listInfo:
                writer.writerow(info)

    def cal_diff(self,startTime, endTime):
        diffTime = float((endTime - startTime).microseconds/1000)
        return diffTime
