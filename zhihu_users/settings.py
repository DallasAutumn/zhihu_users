# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_users project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu_users'

SPIDER_MODULES = ['zhihu_users.spiders']
NEWSPIDER_MODULE = 'zhihu_users.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu_users (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'authority': 'www.zhihu.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'cookie': '_zap=977e2d5c-3d80-4bd4-a3e0-29c6d786c9aa; d_c0="AHAoAhMZXw6PTrKkXAJWZ0IMwK1PwPeAlg8=|1539680083"; _xsrf=hJY9XfxgWDel9ytT8vFH0UCp8S0QJDjV; l_cap_id="YWVlMTgxODgxMzg4NGUzYjg0ZGRjNTQyNjljZDBmZGQ=|1541222719|576440cafb026535e4c348c83c09e6888cc215ae"; r_cap_id="ZWY2ZTEwYWVjNjkyNGVhNDljNTg2ODk4MzA3Zjk4YTE=|1541222719|34f5c57b6e422925eae831e1a7b1dc9880c4b450"; cap_id="MjZiZTcwYjk2ODliNDJhMzkwYTEwMzFjOGYwOTQyZDA=|1541222719|bad9dda88b123b570d16be7432bceaa2ce219e34"; capsion_ticket="2|1:0|10:1541223079|14:capsion_ticket|44:MTU0ODgwMWIyYjIxNDEwMGFlNmI5NWYwMzhjMDU5ZmE=|5aab3da7f4d182d65d9001d19dac98fcdf736121fa96fe7a73b51e15e1eb09bb"; z_c0="2|1:0|10:1541223113|4:z_c0|92:Mi4xM0U1VEJ3QUFBQUFBY0NnQ0V4bGZEaWNBQUFDRUFsVk55YjhFWEFEUnY1WkRZSnNRcERENDVBNUw0cXBhS1l3clp3|51aa7d35c1768d12cb4aba743b48d71f0a392f163dd43ffe37af04066e455aa2"; tst=r; __gads=ID=6ba2edd370f20908:T=1541511382:S=ALNI_Mbp6Jpwr0BncARDB7WJleXd-IIaGw; q_c1=c513ca45f5614395a3404f77ac6ba33c|1543153881000|1539693362000; __utmz=155987696.1543326203.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=155987696.1196878360.1543326203.1543334855.1543407971.3; tgw_l7_route=200d77f3369d188920b797ddf09ec8d1'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihu_users.middlewares.ZhihuUsersSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihu_users.middlewares.ZhihuUsersDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'zhihu_users.pipelines.MySQL_Pipeline': 200,
    'zhihu_users.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MONGO_URI = '10.2.7.108:27324'
MONGO_DATABASE = 'zhihu_info'

SQL_URI = 'localhost'
USER = 'root'
PSWD = 'nativefaith1708'
SQL_DB = 'zhihu_users'
