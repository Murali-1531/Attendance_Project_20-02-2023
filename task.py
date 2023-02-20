from elasticsearch import Elasticsearch
import elasticsearch
import datetime
import json
now = datetime.datetime.now()
es=Elasticsearch([{'host':"localhost",'port':9200,'scheme':"http"}])
def Add(n):
	for i in range(1,n+1):
		name=input("Enter the Name:")	
		m=int(input("Enter the Mark:"))
	res=es.index(index="st_mark",document={"Name":name,"Mark":m,"id":i,"Time":now.isoformat()})
		
res=es.sql.query(body={"query":"select * from st_mark "})
print(type(res))
print (json.dumps(dict(res),sort_keys=True, indent=4))
#print(json.dumps(json.loads(res,indent=4)))
#print(res.get("rows"))
#re=es.delete(index='st_mark',id="tH1WYIQBLdmZp2vZWJt_")
#print(re)
def  Avg():
	res=es.sql.query(body={"query":"SELECT AVG(Mark)FROM st_mark WHERE Time >now()-interval 5 days"})
	print(res)
#Avg()
#n=int(input("Enter the Count:"))
#Add(n)
#Avg()
#doc={"Name":"Kelly","Mark":40,"id":4,"Time":now.isoformat()}
#res=es.update(index="st_mark",id="un2_YIQBLdmZp2vZspsV",doc={"Mark":45})
#print version of elastic search
#print (elasticsearch.VERSION)
