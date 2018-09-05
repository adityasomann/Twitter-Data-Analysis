import json
import re

myfile = open("twit_data_out.txt")
text = myfile.read()
pat = re.compile(r"#(\w+)")
hashes =  pat.findall(text)
print hashes
