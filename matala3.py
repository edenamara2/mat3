f = open('Data_Whatsup.txt','r',encoding='utf-8')
file_mesudar=f.read()
data_muzpan=dict()
The_list=list()
file_mesudar=file_mesudar.split('\n')
id=0


md=dict()

for line in file_mesudar:
    if ":" in line[line.find('-')+2: ]: 
        if line[line.find('-')+2:line.find(': ')] not in data_muzpan:
            id=id+1
            data_muzpan[line[line.find('-')+2:line.find(': ')]]=id    
    data_muzpan['datetime']=line[:line.find("-")-1]
    data_muzpan['id']=id
    data_muzpan['text']= line[line.find(': ')+1: ]
   
    The_list.append({"datetime":data_muzpan['datetime'],"id":data_muzpan['id'],"text": data_muzpan['text']})
The_list
 
for line in file_mesudar:
     if "נוצרה על ידי" in line:
         md['chat name']=line[line.find(' "')+2:line.find('" ')]
         md['date_creation']= line[:line.find('-')-1 ]
         md['num_of_participants']= id
         md['creator']= line[line.find('על ידי ')+9:len(line)-2].rstrip().lstrip() 

am={"md":md, "messages":The_list}  
import json
newjson=json.dumps(am,ensure_ascii=False, indent=5) 
  
with open(md['chat name']+'.txt' ,'w',encoding='utf-8') as f:
  f.write(newjson)