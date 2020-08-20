import os
def create(Project_name="New_Scrapy_Project"):
    path = os.getcwd()
    os.system("cd %s"%path)
    os.system("scrapy startproject %s"%Project_name)