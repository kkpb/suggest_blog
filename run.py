import os

os.chdir("/Users/e105744/Documents/JobHunting/klab/suggest/hatena")
os.system("scrapy crawl --nolog hatena_blog -o ../json/`date +'%Y-%m-%d_%H:%M:%S'`.json")
