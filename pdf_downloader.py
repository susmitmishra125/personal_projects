import os
from scidownl.scihub import *#pip3 install -U scidownl
#reference    https://pypi.org/project/scidownl/
link="https://sci-hub.se/"
out='paper'
dirname = os.path.dirname(__file__)
f=open(os.path.join(dirname,'doi.txt'),'r').read().split()
i=0

while i<len(f) :
	try:
		SciHub(f[i],out).download(choose_scihub_url_index=3)
		i=i+1
		print(i,"completed")
	except:
		print("Oops error occured trying again")
print("Done downloading all files")