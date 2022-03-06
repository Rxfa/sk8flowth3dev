import gzip
import os
import io
 
name = 'sample.py.gz'
 
with gzip.open(name, 'rb') as ip:
        with io.TextIOWrapper(ip, encoding='utf-8') as decoder:
            # Let's read the content using read()
            content = decoder.read()
            filein = open("imhere.py","a")
            filein.write(content)
            #filein.close()
            #print(content)