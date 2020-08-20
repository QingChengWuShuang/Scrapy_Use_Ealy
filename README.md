# Scrapy_Use_Ealy
一个创建Scrapy项目,创建Scrapy爬虫,运行爬虫的库，欢迎大家修改

说明文档
---
 * __init__.py 
 
没有什么卵用的一个文件


---
* Create_Scrapy_Project.py 

创建Scrapy项目的文件

内含一个函数create，调用函数需要传递一个可选参数，也就是项目名称。

调用函数后将在此py文件的同级目录下创建一个scrapy项目

---

* Create_Scrapy_Spider.py

内含一个函数create_Spider,需要传递两个参数，一个是爬虫的名字，另一个是url

运行此函数的py文件应该在和scrapy.cfg在同级目录下。

实例

假如我创建一个项目叫Project，我需要把运行此函数的py文件放在

> Project
>> Project

>> scrapy.cfg

>> 运行函数的py文件

---
* Run_Scrapy_Spider

建议执行其中的run函数

run函数有两个参数，name参数需要传递爬虫的名称，log参数是是否记录日志，True则记录日志，False则不记录日志，

默认是True,如果是True的话，将在此文件的同级目录下创建一个logs.txt来保存日志，

运行此函数的py文件应该在和scrapy.cfg在同级目录下。

> Project
>> Project

>> scrapy.cfg

>> 运行爬虫的py文件

---

* Maybe.url.py

保存了一些你创建爬虫时可能用到的url


---

* Scrapy_Headers.py

！！！
您还在担心每次创建的时候都需要到刘篮球复制User-Agent吗？？？
快，在settings.py导入这个几乎万能的headers（有些时候可能行不通，还得自己写headers，这只是一个基本框架），调用其中的变量`headers`吧！

---




## Finish!
