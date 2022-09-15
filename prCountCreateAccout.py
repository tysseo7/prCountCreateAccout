
#### pip install requests

import json
import requests
import sys

args = sys.argv
ll=int(args[1])
nn=int(args[2])


for num in range(nn):
  ll = ll - num
  url = "https://api.mainnet.minepi.com/ledgers/" + str(ll) + "/operations"
  #url = "https://api.mainnet.minepi.com/ledgers/4712031/operations"
  session = requests.Session()
  dd = session.get(url)
  json_data = json.loads(dd.text)
  #print(dd.text)
  #print(type(dd.text))  #str
  jd=json_data
  l_r=jd['_embedded']['records']
  if len(l_r) == 0 :
    print(
     str(ll) 
     + ", " + str(c_tp) 
     + ", " + "NULL" 
     + ", ... ledger, num of create_account, time"
    )
    continue

  c_tp=0
  for xx in l_r:
    tp=xx['type']
    if tp=="create_account":
      c_tp=c_tp+1

  print(
   str(ll) 
   + ", " + str(c_tp) 
   + ", " + l_r[len(l_r)-1]['created_at'] 
   + ", ... ledger, num of create_account, time"
  )




# 