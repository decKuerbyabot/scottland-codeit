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
        if i==0:
            rates_row=[pr["flow_rate"]]
        else:
            for j in range(i):
                if j-1<0:
                    rates_row[j]=rates[i-1][j]/2
                else:
                    rates_row[j]=(rates[i-1][j]+rates[i-1][j-1])/2
        rates.append(rates_row)

    full_times=[]
    for i in range(pr["row_number"]):
        if i==0:
            times_row=[100/pr["flow_rate"]]

            times_row=[0]
        else:
            for j in range(i):
                if j-1<0:
                    rates_row[j]=rates[i-1][j]/2
                else:
                    rates_row[j]=(rates[i-1][j]+rates[i-1][j-1])/2
        rates.append(rates_row)



    # row=pr["row_number"]
    col=pr["col_number"]
    pass

def see_if_full_p1(row, col, t):
    pass



def find_full_time_p1(row, col, full_times, rates):
    if row-1<0:
        return 
    elif col-1<0:
        upper_full=find_full_time_p1(row-1, col)
        upper_rate=rates[row-1][col]

    else:
        uf1=find_full_time_p1(row-1, col-1)
        uf2=find_full_time_p1(row-1, col)

        ur1=rates[row-1][col]
        ur2=rates[row-1][col-1]
        uf_soon=min(uf1, uf2)
        uf_late=max(uf1, uf2)
        ur_soon=max(ur1, ur2)
        ur_late=min(ur2, ur1)




        
    find_full_time_p1(row-1, col-1)

def solve_part2():
    pass


def solve_part3():
    pass

def solve_part4():
    pass

