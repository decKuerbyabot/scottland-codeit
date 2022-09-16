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
    temp = sorted([i.split(',') for i in stream], key=lambda x: (x[0], x[1]))
    ticker_dict = {}
    res = []
    for i in temp:
        if i[1] not in ticker_dict:
            ticker_dict[i[1]] = {}
            ticker_dict[i[1]]['q'] = 0
            ticker_dict[i[1]]['p'] = 0

        count = int(i[2])
        while count > 0:
            if ticker_dict[i[1]]['q'] + count >= quantity_block:
                ticker_dict[i[1]]['p'] = round(
                    ticker_dict[i[1]]['p'] +
                    (quantity_block - ticker_dict[i[1]]['q']) * float(i[3]), 2)
                count -= (quantity_block - ticker_dict[i[1]]['q'])
                res.append(i[0] + ',' + i[1] + ',' + str(quantity_block) +
                           ',' + str(ticker_dict[i[1]]['p']))
                ticker_dict[i[1]]['q'] = 0
                ticker_dict[i[1]]['p'] = 0
            else:
                ticker_dict[i[1]]['q'] += count
                ticker_dict[i[1]]['p'] = round(
                    ticker_dict[i[1]]['p'] + count * float(i[3]), 2)
                break
    return res