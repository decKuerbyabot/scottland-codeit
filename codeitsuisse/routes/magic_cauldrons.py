import sys

def find_full_time_p1(row, col, full_times, rates):
    if row==0 and col==0:
        return 100/rates[0][0]
    elif full_times[row][col]==0:
        uftl=sys.float_info.max if col==0 else find_full_time_p1(row-1, col-1, full_times, rates)
        uftr=sys.float_info.max if col==row else find_full_time_p1(row-1, col, full_times, rates)
        url=0 if col==0 else rates[row-1][col-1]
        urr=0 if col==row else rates[row-1][col]
        this_full_time=(200+url*uftl+urr*uftr)/(url+urr)
        full_times[row][col]=this_full_time
        return this_full_time
    else:
        return full_times[row][col]

def find_full_time_p2(row, col, full_times, rates):
    if row==0 and col==0:
        return 150/rates[0][0]
    elif full_times[row][col]==0:
        uftl=sys.float_info.max if col==0 else find_full_time_p2(row-1, col-1, full_times, rates)
        uftr=sys.float_info.max if col==row else find_full_time_p2(row-1, col, full_times, rates)
        url=0 if col==0 else rates[row-1][col-1]
        urr=0 if col==row else rates[row-1][col]
        if col%2==0:
            this_full_time=(300+url*uftl+urr*uftr)/(url+urr)
            # print("calculated full time", this_full_time)
        else:
            this_full_time=(200+url*uftl+urr*uftr)/(url+urr)
        full_times[row][col]=this_full_time
        # print(full_times)
        return this_full_time
    else:
        return full_times[row][col]
   
        

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

    col=pr["col_number"]
    row=pr["row_number"]
    time=pr["time"]
    rate=pr["flow_rate"]


    rates=[]
    for i in range(row+1):
        rates_row=[]
        if i==0:
            rates_row=[rate]
        else:
            for j in range(i+1):
                if j-1<0:
                    rates_row.append(rates[i-1][j]/2)
                elif j>=i:
                    rates_row.append(rates[i-1][j-1]/2)
                else:
                    rates_row.append((rates[i-1][j]+rates[i-1][j-1])/2)
        rates.append(rates_row)

    full_times=[]
    for i in range(row+1):
        times_row=[]
        if i==0:
            times_row=[100/rate]
        else:
            for j in range(i+1):

                times_row.append(0)
        full_times.append(times_row)
    
    full_time=find_full_time_p1(row,col, full_times, rates)
    # print(full_time)
    if full_time<=pr["time"]:
        return 100
    else:
        upper_time_l= sys.float_info.max if col==0 else find_full_time_p1(row-1, col-1, full_times, rates)
        upper_time_r= sys.float_info.max if col>=row else find_full_time_p1(row-1, col, full_times, rates)
        upper_rate_l= 0 if col==0 else rates[row-1][col-1]
        upper_rate_r = 0 if col==row else rates[row-1][col]
        # print(full_times)
        # print(upper_full_time_l)
        # print(upper_full_time_r)
        return max(0, time-upper_time_l) * upper_rate_l/2 + max(0, time-upper_time_r)*upper_rate_r/2

def solve_part2(pr):
    row=pr["row_number"]
    col= pr["col_number"]
    amount=pr["amount_of_soup"]
    rate=pr["flow_rate"]
    rates=[]
    for i in range(row+1):
        rates_row=[]
        if i==0:
            rates_row=[rate]
        else:
            for j in range(i+1):
                if j-1<0:
                    rates_row.append(rates[i-1][j]/2)
                elif j>=i:
                    rates_row.append(rates[i-1][j-1]/2)
                else:
                    rates_row.append((rates[i-1][j]+rates[i-1][j-1])/2)
        rates.append(rates_row)

    full_times=[]
    for i in range(row+1):
        times_row=[]
        if i==0:
            times_row=[100/rate]
        else:
            for j in range(i+1):

                times_row.append(0)
        full_times.append(times_row)
    
    upper_time_l= sys.float_info.max if col==0 else find_full_time_p1(row-1, col-1, full_times, rates)
    upper_time_r= sys.float_info.max if col>=row else find_full_time_p1(row-1, col, full_times, rates)
    upper_rate_l= 0 if col==0 else rates[row-1][col-1]
    upper_rate_r = 0 if col==row else rates[row-1][col]

    fill=(upper_time_l-upper_time_r)*upper_rate_r/2 if upper_time_l>upper_time_r else (upper_time_r-upper_time_l)*upper_rate_l/2
    if fill>amount:
        time = upper_time_l+2*amount/upper_rate_l if upper_time_l<upper_time_r else upper_time_r+2*amount/upper_rate_r
        return time
    else:
        return (2*amount+upper_time_l*upper_rate_l+upper_time_r*upper_rate_r)/(upper_rate_l+upper_rate_r)

    return (2*amount+upper_time_l*upper_rate_l+upper_time_r*upper_rate_r)/(upper_rate_l+upper_rate_r)

def solve_part3(pr):
    col=pr["col_number"]
    row=pr["row_number"]
    time=pr["time"]
    rate=pr["flow_rate"]

    rates=[]
    for i in range(row+1):
        rates_row=[]
        if i==0:
            rates_row=[rate]
        else:
            for j in range(i+1):
                if j-1<0:
                    rates_row.append(rates[i-1][j]/2)
                elif j>=i:
                    rates_row.append(rates[i-1][j-1]/2)
                else:
                    rates_row.append((rates[i-1][j]+rates[i-1][j-1])/2)
        rates.append(rates_row)

    # initialize full times array
    full_times=[]
    for i in range(row+1):
        times_row=[]
        if i==0:
            times_row=[150/rate]
        else:
            for j in range(i+1):
                times_row.append(0)
        full_times.append(times_row)

    full_time=find_full_time_p2(row, col, full_times, rates)
    # print(row)
    # print(col)
    # print("found Full time 2 1", find_full_time_p2(2,1,full_times, rates))
    # print(full_times)

    # print("p4 ft", full_time)
    if full_time<=time:
        return 150 if col%2==0 else 100
    else:
        upper_time_l= float('inf') if col==0 else find_full_time_p2(row-1, col-1, full_times, rates)
        # print("p4 utl",upper_time_l)
        upper_time_r= float("inf") if col>=row else find_full_time_p2(row-1, col, full_times, rates)
        # print("p4 utr",upper_time_r)
        upper_rate_l= 0 if col==0 else rates[row-1][col-1]
        upper_rate_r = 0 if col==row else rates[row-1][col]
        return max(0, time-upper_time_l) * upper_rate_l/2 + max(0, time-upper_time_r)*upper_rate_r/2
    
def solve_part4(pr):
    col=pr["col_number"]
    row=pr["row_number"]
    amount=pr["amount_of_soup"]
    rate=pr["flow_rate"]

    rates=[]
    for i in range(row+1):
        rates_row=[]
        if i==0:
            rates_row=[rate]
        else:
            for j in range(i+1):
                if j-1<0:
                    rates_row.append(rates[i-1][j]/2)
                elif j>=i:
                    rates_row.append(rates[i-1][j-1]/2)
                else:
                    rates_row.append((rates[i-1][j]+rates[i-1][j-1])/2)
        rates.append(rates_row)
    # print(rates)
    # initialize full times array
    full_times=[]
    for i in range(row+1):
        times_row=[]
        if i==0:
            times_row=[150/rate]
        else:
            for j in range(i+1):

                times_row.append(0)
        full_times.append(times_row)
    
    # print("found Full time 2 1", find_full_time_p2(2,1,full_times, rates))
    
    uts=dict()
    upper_time_l= sys.float_info.max if col==0 else find_full_time_p2(row-1, col-1, full_times, rates)
    upper_time_r= sys.float_info.max if col>=row else find_full_time_p2(row-1, col, full_times, rates)
    upper_rate_l= 0 if col==0 else rates[row-1][col-1]
    upper_rate_r = 0 if col==row else rates[row-1][col]
    # uts["l"]=upper_time_l
    # uts["r"]=upper_time_r
    fill=(upper_time_l-upper_time_r)*upper_rate_r/2 if upper_time_l>upper_time_r else (upper_time_r-upper_time_l)*upper_rate_l/2
    if fill>amount:
        time = upper_time_l+2*amount/upper_rate_l if upper_time_l<upper_time_r else upper_time_r+2*amount/upper_rate_r
        return time
    else:
        return (2*amount+upper_time_l*upper_rate_l+upper_time_r*upper_rate_r)/(upper_rate_l+upper_rate_r)
 
        
        # if fill>amount:
        #     return 
        
    


    # print("utl", upper_time_l)
    # print("utr", upper_time_r)
    
    # print("url", )
    # print(full_times)
    # print("ul", upper_time_l)
    # print("ur", upper_time_r)
    # print("ul", upper_rate_l)
    # print("ur", upper_rate_r)
    # print("amount", amount)
    # print("upper", 2*amount+upper_time_l*upper_rate_l+upper_time_r*upper_rate_r)
    # print("lower", upper_rate_l+upper_rate_r)

if __name__=="__main__":
    print("p1", solve_part1({
      "flow_rate": 20,
      "time": 6,
      "row_number": 1,
      "col_number": 1
    }))

    print("p1", solve_part1({
      "flow_rate": 20,
      "time": 40,
      "row_number": 3,
      "col_number": 2
    }))

    print("p2", solve_part2({
      "flow_rate": 20,
      "amount_of_soup": 87.5,
      "row_number": 3,
      "col_number": 1
    }))

    print("p2 5 1 1 shoule be 5.5", solve_part2({
      "flow_rate": 20,
      "amount_of_soup": 5,
      "row_number": 1,
      "col_number": 1
    }))

    print("p2 100 1 1 shoule be 15", solve_part2({
      "flow_rate": 20,
      "amount_of_soup": 100,
      "row_number": 1,
      "col_number": 1
    }))

    print("p3", solve_part3({
      "flow_rate": 20,
      "time": 7.5,
      "row_number": 2,
      "col_number": 2
    }))

    print("p3 40 3 2 should be 50", solve_part3({
      "flow_rate": 20,
      "time": 40,
      "row_number": 3,
      "col_number": 2
    }))

    print("p3 55.83 3 2 should be 150", solve_part3({
      "flow_rate": 20,
      "time": 55.83,
      "row_number": 3,
      "col_number": 2
    }))

    print("p4 150 3 2 should be 55.83", solve_part4({
      "flow_rate": 20,
      "amount_of_soup": 150,
      "row_number": 3,
      "col_number": 2
    }))


    print("p4 100 1 1 should be 17.5", solve_part4({
      "flow_rate": 20,
      "amount_of_soup": 100,
      "row_number": 1,
      "col_number": 1
    }))

    print("p4 50 3 2 should be 40", solve_part4({
      "flow_rate": 20,
      "amount_of_soup": 50,
      "row_number": 3,
      "col_number": 2
    }))

    print("p4 100 0 1 should be 17.5", solve_part4({
      "flow_rate": 20,
      "amount_of_soup": 100,
      "row_number": 1,
      "col_number": 1
    }))

    print("p4 150 0 1 should be 22.5", solve_part4({
      "flow_rate": 20,
      "amount_of_soup": 150,
      "row_number": 1,
      "col_number": 1
    }))

    print("p4 5 1 1 shoule be 8", solve_part4({
      "flow_rate": 20,
      "amount_of_soup": 5,
      "row_number": 1,
      "col_number": 1
    }))

    print(solve_case({
    "part1":{
        "flow_rate": 20,
        "time": 6,
        "row_number": 1,
        "col_number": 1
        },
    "part2":{
        "flow_rate": 20,
        "amount_of_soup": 5,
        "row_number": 1,
        "col_number": 1
        },
    "part3":{
        "flow_rate": 20,
        "time": 40,
        "row_number": 3,
        "col_number": 2
    },
    "part4":{
        "flow_rate": 20,
        "amount_of_soup": 50,
        "row_number": 3,
        "col_number": 2
    }
    }))

    # print(solve)



