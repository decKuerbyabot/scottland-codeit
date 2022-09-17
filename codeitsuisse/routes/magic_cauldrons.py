def solve_magic_cauldron(input):
    ans=[]
    for test_case in input:
        ans.append(solve_case(test_case))
    return ans



def solve_case(test_case):


    return {
        "part1":solve_part1(test_case["part1"]),
        "part2":solve_part2(test_case["part2"]),
        "part3":solve_part3(test_case["part3"]),
        "part4":solve_part4(test_case["part4"])
    }
    






def solve_part1(pr):
    rates=[]
    for i in range(pr["row_number"]):
        rates_row=[]
        for j in range(99):
            if i==0:
                pass

    row=pr["row_number"]
    col=pr["col_number"]
    pass

def see_if_full_p1(row, col, t):
    pass



def find_full_time_p1(row, col):
    if row-1<0:
        return 1
    elif col-1<0:
        upper_full=find_full_time_p1(row-1, col)

    else:
        uf1=find_full_time_p1(row-1, col-1)
        uf2=find_full_time_p1(row-1, col)
        uf_soon=min(uf1, uf2)
        uf_late=max(uf1, uf2)
        ur_soon=1


        
    find_full_time_p1(row-1, col-1)

def solve_part2():
    pass


def solve_part3():
    pass

def solve_part4():
    pass

