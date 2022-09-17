# import logging
# from flask import request, jsonify
# from codeitsuisse import app
# import copy

# logger = logging.getLogger(__name__)


def solve_cryptocollapz(lol):
    sol=[]
    for l in lol:
        l_sol=[]
        for n in l:
            l_sol.append(int(find_max(n)))
        sol.append(l_sol)
    return sol


def find_max(x):
    if x==4:
       return x
    elif x%2==0:
        return max(find_max(x/2), x)
    else:
        return max(find_max(3*x+1), x)

if __name__=="__main__":
    input=[
        [ 1, 2, 3, 4, 5 ],
        [ 6, 7, 8, 9, 10 ],
    ]
    output=[
        [ 4, 4, 16, 4, 16 ],
        [ 16, 52, 8, 52, 16 ],
    ]
    print(solve(input))
