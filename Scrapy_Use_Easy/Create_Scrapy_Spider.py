import os
import Scrapy_Use_Easy
def create_Spider(Spider_Name,url):
    os.system("cd %s"%os.getcwd())
    os.system('scrapy genspider %s "%s"'%(Spider_Name,url))