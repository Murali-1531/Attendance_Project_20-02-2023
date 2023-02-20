from elasticsearch import Elasticsearch as es
x = es([{'host': 'localhost', 'port':9200, 'scheme':'http'}])
#insert Data into Index
#for i in range(1,6):
#	name=input("Enter The Name:")
#	regno=int(input("Enter The Regno:"))
#	doc={"Name":name,"Reg":regno}
#	res=x.index(index='student',id=i,document=doc)
#Display Data
#res=x.sql.query(body={"query":"select * from student"})
#for i in range(len(res.get("rows"))):
#	print(res.get("rows")[i])
res=x.update(index='student',id="un2_YIQBLdmZp2vZspsV",doc={"doc":{"Mark":25}})


