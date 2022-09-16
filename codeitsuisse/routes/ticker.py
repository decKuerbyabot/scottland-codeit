import logging
from flask import request, jsonify
from codeitsuisse import app
import copy

logger = logging.getLogger(__name__)

def to_cumulative(stream: list):
    temp = sorted([i.split(',') for i in stream], key=lambda x: (x[0], x[1]))
    ticker_dict = {}
    stream_dict = {}

    for i in temp:
        if i[0] not in stream_dict:
            stream_dict[i[0]] = {}
        if i[1] not in stream_dict[i[0]]:
            stream_dict[i[0]][i[1]] = {'p':0,'q':0}
        if i[1] not in ticker_dict:
            ticker_dict[i[1]] = {'p':0,'q':0}
        ticker_dict[i[1]]['q'] += int(i[2])
        stream_dict[i[0]][i[1]]['q'] = ticker_dict[i[1]]['q']
        ticker_dict[i[1]]['p'] = round(ticker_dict[i[1]]['p'] + int(i[2]) * float(i[3]),2)
        stream_dict[i[0]][i[1]]['p'] = ticker_dict[i[1]]['p']

    res = []
    for i in stream_dict:
        temp = i
        for j in stream_dict[i]:
            temp += ',' + j + ','
            temp += str(stream_dict[i][j]['q']) + ','
            temp += str(stream_dict[i][j]['p'])
        res.append(temp)
    return res


def to_cumulative_delayed(stream: list, quantity_block: int):
  stream=sorted(stream, key=lambda s: s.split(',')[0]+s.split(',')[1])
  stream=[s.split(',') for s in stream]
  res_dict=dict()

  res=[]
  for s in stream:
    if s[1] not in res_dict.keys():
      res_dict[s[1]]=dict()
      res_dict[s[1]]['t']='00:00'
      res_dict[s[1]]['q']=0
      res_dict[s[1]]['v']=0
  
  #for num in range(int())
    single_count=int(s[2])
    while single_count>0:
      if res_dict[s[1]]['q']+single_count>=quantity_block:
        res_dict[s[1]]['v']+=(quantity_block-res_dict[s[1]]['q'])*float(s[3])
        single_count-=quantity_block-res_dict[s[1]]['q']
        res.append(s[0]+','+s[1]+','+str(quantity_block)+','+str(res_dict[s[1]]['v']))
        res_dict[s[1]]=dict()
        res_dict[s[1]]['t']=s[0]
        res_dict[s[1]]['q']=0
        res_dict[s[1]]['v']=0
      else:
        res_dict[s[1]]['t']=s[0]
        res_dict[s[1]]['q']+=single_count
        res_dict[s[1]]['v']+=single_count*float(s[3])
        break

  return res