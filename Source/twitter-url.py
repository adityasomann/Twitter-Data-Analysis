import json
import re

myfile = open("twit_data_out.txt")
text = myfile.read()
#urls =re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
urls = re.findall("((www\.|http://|https://)(www\.)*.*?(?=(www\.|http://|https://|$)))", text)
print urls
