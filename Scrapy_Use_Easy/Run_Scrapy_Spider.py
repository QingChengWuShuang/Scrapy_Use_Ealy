import datetime
import os
def run_spider(name):
    print("Run Spider %s" % name)
    os.system("cd %s" % os.getcwd())
    os.system("scrapy crawl %s" % name)
    print("Finish crawl!")
def run(name,log=True):
    if log:
        print("Write Logs at logs.txt")
        run_spider(name)
        with open(os.getcwd()+"\logs.txt", 'a') as fp:
            fp.write("Run %s Spider At %s!\n"%(name,datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')))
    else:
        run_spider(name)


