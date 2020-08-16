# Amazon-Crawling

```sh
# Linux/ MacOS
chmod +x run.sh
./run.sh

#Windows
#to execute crawling
scrapy crawl amazon -o AmazonCrawlData.json
#to refine data
env/bin/python3.8 AZCrawling/fileHandling.py

#pip Library
python -m pip install scrapy
python -m pip install termcolor
```



###### Terminal Look:

```bash
$ ./run.sh
What you Want to search : DSLR
-----
	.....
	.....
	.....
	2020-08-16 21:45:23 [scrapy.core.engine] INFO: Spider closed (finished)
-----
$
```



**Note: **

> AmazonCrawlData.json : It contains unstructured retrived data.
>
> RefineJSON.json : Refined into structured data.



<img src="https://github.com/PushpanshuRanjanSingh/Amazon-Crawling/blob/master/refined.png" style="zoom:33%;" />

​																							<u>Refined Structured Data</u>



<img src="https://github.com/PushpanshuRanjanSingh/Amazon-Crawling/blob/master/rawdata.png" style="zoom:33%;" />

​																					<u>Raw Unstructed Data</u>