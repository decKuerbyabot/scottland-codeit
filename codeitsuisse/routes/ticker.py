import logging
from flask import request, jsonify
from codeitsuisse import app
import copy

logger = logging.getLogger(__name__)

@app.route('/tickerStreamPart1', methods=['POST'])
def part_1():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # result = []
    ans = to_cumulative(data)

    # for test_case in data:
        # result.append(ans)
    logging.info("My result :{}".format(ans))
    return jsonify(ans)

@app.route('/tickerStreamPart2', methods=['POST'])
def part_2():
    # data = request.get_json()
    # logging.info("data sent for evaluation {}".format(data))
    # result = []
    # ans = to_cumulative(data)

    # for test_case in data:
    #     result.append(ans)
    # logging.info("My result :{}".format(result))
    # return jsonify(result)
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = to_cumulative_delayed(data["stream"])
    logging.info("My result :{}".format(ans))
    return jsonify({"output": ans})


def to_cumulative(stream: list):
  # print(stream)
  stream=sorted(stream, key=lambda s: s.split(',')[0]+s.split(',')[1])
  stream=[s.split(',') for s in stream]
  res_dict=dict()
  for s in stream:
    if s[0] not in res_dict.keys():
      if len(res_dict.keys())==0:
        res_dict[s[0]]=dict()
      else:
        res_dict[s[0]]=copy.deepcopy(res_dict[list(res_dict.keys())[-1]])
    if s[1] not in res_dict[s[0]].keys():
      res_dict[s[0]][s[1]]=dict()
      res_dict[s[0]][s[1]]["q"]=0
      res_dict[s[0]][s[1]]["v"]=0
    res_dict[s[0]][s[1]]["q"]+=int(s[2])
    res_dict[s[0]][s[1]]["v"]+=float(s[3])*int(s[2])
  res=[]
  for i in res_dict.keys():
    s=i+",";
    for j in res_dict[i].keys():
      s+=j
      s+=","
      s+=str(res_dict[i][j]['q'])
      s+=","
      s+=str(res_dict[i][j]['v'])
      s+=","
    s=s[:-1]
    res.append(s)
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