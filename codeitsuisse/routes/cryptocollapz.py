# import logging
# from flask import request, jsonify
# from codeitsuisse import app
# import copy

# logger = logging.getLogger(__name__)


from cgitb import lookup


def solve_cryptocollapz(lol):
    lookup_table=dict()
    sol=[]
    for l in lol:
        l_sol=[]
        for n in l:
            if n not in lookup_table.keys():
                maxval=find_max(n, lookup_table)
                l_sol.append(int(maxval))
                lookup_table[n]=maxval
            else:
                l_sol.append(lookup_table[n])
        sol.append(l_sol)
    return sol


def find_max(x, lt):
    if x==4:
       return x
    elif x%2==0:
        halfval=int(x/2)
        if halfval in lt.keys():
            maxhalf=lt[halfval]
        else:
            maxhalf=find_max(halfval, lt)
            lt[halfval]=maxhalf
        return max(maxhalf, x)
    else:
        halfval=3*x+1
        if halfval in lt.keys():
            maxhalf=lt[halfval]
        else:
            maxhalf=find_max(halfval, lt)
            lt[halfval]=maxhalf
        return max(maxhalf, x)


if __name__=="__main__":
    input=[

        [ 1, 2, 3, 4, 5 ],
        # [ 10000, 10000, 10000, 10000, 10000],
    ]
    input_1=[]
    # for i in range(100000):
        # input_1.append([ 901294, 182913, 289123, 281942, 882132])
    
    output=[
        [ 4, 4, 16, 4, 16 ],
        [ 16, 52, 8, 52, 16 ],
    ]
    print(solve_cryptocollapz(input))
    # print(solve_cryptocollapz(input_1))

