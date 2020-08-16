#!/bin/bash

scrapy crawl amazon -o AmazonCrawlData.json;
env/bin/python3.8 AZCrawling/fileHandling.py