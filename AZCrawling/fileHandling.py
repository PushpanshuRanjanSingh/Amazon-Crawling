import json
import os
from  termcolor import cprint, colored

def handleFile():
        f= open(os.path.expanduser('~/Desktop/Intern/AZCrawling/AmazonCrawlData.json'),'r')
        jsonData = json.load(f)
        f.close()
        RefineData = {}
        index=0
        for data in jsonData:
            for i in range(len(data['Title'])):
                # Colored Output
                # try:
                #     title = colored(data['Title'][i][:100], 'red')
                #     price = colored(data['Price'][i], 'cyan')
                #     stars = colored(data['Stars'][i],'yellow')
                #     image = colored(data['Image'][i], 'blue')
                #     print(title,price,stars,image)
                # except BaseException:
                #     continue

                try:
                    title = data['Title'][i][:100]
                    price = data['Price'][i]
                    stars = data['Stars'][i]
                    image = data['Image'][i]
                except BaseException:
                    continue

                dict={
                    'Title': title,
                    'Price': price,
                    'Stars': stars,
                    'Image': image
                }
                RefineData[index]= dict
                index+=1
        with open('RefineJSON.json', 'a') as f:
            json.dump(RefineData, f)


handleFile()