import os

os.chdir("./hatena")
os.system("scrapy crawl hatena_blog -o ../json/`date +'%Y-%m-%d_%H:%M:%S'`.json")
