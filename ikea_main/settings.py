import os
from .random_proxy import get_random_proxy

BOT_NAME = 'ikea_main'

SPIDER_MODULES = ['ikea_main.spiders']
NEWSPIDER_MODULE = 'ikea_main.spiders'
# PROXY_USER = 'rimal'
# PROXY_PASSWORD = 'Kha2H5wnnX'
# PROXY_URL = get_random_proxy()
# PROXY_PORT = '60000'
# print(PROXY_URL)
# # Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
#LOG_LEVEL = 'INFO'
LOG_FILE = 'log.txt'
LOG_FILE_APPEND = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 320


# DOWNLOADER_MIDDLEWARES = {
#    'ikea_main.middlewares.ProxyMiddleware': 100,
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
# }



REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

FEED_EXPORT_FIELDS = [
    'scrap_url',
    'category',
    'brand',
    'name',
    'product_code',
    'price',
    'list_price',
    'qty',
    'description',
    'image1',
    'image2',
    'image3',
    'image4',
    'image5',
    'image6',
    'image7',
    'image8',
    'image9',
    'image10',
]