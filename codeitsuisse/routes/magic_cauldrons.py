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
        upper_full_time_l=float("inf")
        upper_rate_l=0
        upper_full_time_r=float("inf")
        upper_rate_r=0
        if col==0:
            upper_full_time_r=find_full_time_p1(row-1, col, full_times, rates)
            upper_rate_r=rates[row-1][col]
            upper_full_time_l=float("inf")
            upper_rate_l=0
        elif col>=row:
            upper_full_time_l=find_full_time_p1(row-1, col-1, full_times, rates)
            upper_rate_l=rates[row-1][col-1]
            upper_full_time_r=float("inf")
            upper_rate_r=0

        else:
            print("Hello")
            upper_full_time_r=find_full_time_p1(row-1, col, full_times, rates)
            # print("upper_full_time_l)

            upper_rate_r=rates[row-1][col]
            upper_full_time_l=find_full_time_p1(row-1, col-1, full_times, rates)
            upper_rate_l=rates[row-1][col-1]
        
        print(full_times)
        print(upper_full_time_l)
        print(upper_full_time_r)
        return max(0, time-upper_full_time_l) * upper_rate_l/2 + max(0, time-upper_full_time_r)*upper_rate_r/2
        
    

def find_full_time_p1(row, col, full_times, rates):
    if row==0:
        return full_times[0][0]
    elif col-1<0:
        if full_times[row][col]==0:
            upper_full=find_full_time_p1(row-1, col, full_times, rates)
            # upper_rate=rates[row-1][col]
            this_full_time=upper_full+100/rates[row][col]
            full_times[row][col]=this_full_time
            return this_full_time
        else:
            return full_times[row][col]
    elif col>=row:
        if full_times[row][col]==0:
            upper_full=find_full_time_p1(row-1, col-1, full_times, rates)
            # upper_rate=rates[row-1][col]
            this_full_time=upper_full+100/rates[row][col]
            full_times[row][col]=this_full_time
            return this_full_time
        else:
            return full_times[row][col]
    else:
        if full_times[row][col]==0:
            uf1=find_full_time_p1(row-1, col-1, full_times, rates)
            uf2=find_full_time_p1(row-1, col, full_times, rates)
            ur1=rates[row-1][col]
            ur2=rates[row-1][col-1]
            uf_soon=min(uf1, uf2)
            uf_late=max(uf1, uf2)
            ur_soon=max(ur1, ur2)
            ur_late=min(ur2, ur1)
            this_full_time=(200+ur_soon*uf_soon+ur_late*uf_late)/(ur_soon+ur_late)
            full_times[row][col]=this_full_time
            return this_full_time
        else:
            return full_times[row][col]
        
    find_full_time_p1(row-1, col-1)

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
    
    upper_time_l= float('inf') if col==0 else find_full_time_p1(row-1, col-1, full_times, rates)
    upper_time_r= float("inf") if col>=row else find_full_time_p1(row-1, col, full_times, rates)
    upper_rate_l= 0 if col==0 else rates[row-1][col-1]
    upper_rate_r = 0 if col==row else rates[row-1][col]

    return (2*amount+upper_time_l*upper_rate_l+upper_time_r*upper_rate_r)/(upper_rate_l+upper_rate_r)


def find_full_time_p2(row, col, full_times, rates):
    if row==0:
        return full_times[0][0]
    elif col==0:
        if full_times[row][col]==0:
            upper_full=find_full_time_p2(row-1, col, full_times, rates)
            # upper_rate=rates[row-1][col]
            this_full_time=upper_full+150/rates[row][col]
            full_times[row][col]=this_full_time
            return this_full_time
        else:
            return full_times[row][col]
    elif col==row:
        if full_times[row][col]==0:
            upper_full=find_full_time_p2(row-1, col-1, full_times, rates)
            # upper_rate=rates[row-1][col]
            if col%2==0:
                this_full_time=upper_full+150/rates[row][col]
            else:
                this_full_time=upper_full+100/rates[row][col]
            full_times[row][col]=this_full_time
            return this_full_time
        else:
            return full_times[row][col]
    else:
        if full_times[row][col]==0:
            uf1=find_full_time_p2(row-1, col-1, full_times, rates)
            uf2=find_full_time_p2(row-1, col, full_times, rates)
            ur1=rates[row-1][col]
            ur2=rates[row-1][col-1]
            uf_soon=min(uf1, uf2)
            uf_late=max(uf1, uf2)
            ur_soon=max(ur1, ur2)
            ur_late=min(ur2, ur1)
            if row%2==0:
                this_full_time=(300+ur_soon*uf_soon+ur_late*uf_late)/(ur_soon+ur_late)
            else:
                this_full_time=(200+ur_soon*uf_soon+ur_late*uf_late)/(ur_soon+ur_late)
            full_times[row][col]=this_full_time
            return this_full_time
        else:
            return full_times[row][col]


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
            times_row=[100/rate]
        else:
            for j in range(i+1):

                times_row.append(0)
        full_times.append(times_row)

    full_time=find_full_time_p2(row-1, col-1, full_times, rates)

    if full_time<=time:
        return 150 if col%2==0 else 100
    else:
        upper_time_l= float('inf') if col==0 else find_full_time_p1(row-1, col-1, full_times, rates)
        upper_time_r= float("inf") if col>=row else find_full_time_p1(row-1, col, full_times, rates)
        upper_rate_l= 0 if col==0 else rates[row-1][col-1]
        upper_rate_r = 0 if col==row else rates[row-1][col]
        return max(0, time-upper_time_l) * upper_rate_l/2 + max(0, time-upper_time_r)*upper_rate_r/2
    
    
def solve_part4():
    pass


if __name__=="__main__":
    # solve part 1 test
    solve_part1({
      "flow_rate": 20,
      "time": 5,
      "row_number": 1,
      "col_number": 0
    })
    solve_part1({
      "flow_rate": 20,
      "time": 5,
      "row_number": 1,
      "col_number": 1
    })
    # solve_part1({
    #   "flow_rate": 20,
    #   "time": 1,
    #   "row_number": 1,
    #   "col_number": 1
    # })

    # solve_part1({
    #   "flow_rate": 20,
    #   "time": 1,
    #   "row_number": 3,
    #   "col_number": 3
    # })
    # print(solve_part1({
    #   "flow_rate": 20,
    #   "time": 1,
    #   "row_number": 3,
    #   "col_number": 2
    # }))

    # print(solve_part1({
    #   "flow_rate": 20,
    #   "time": 40,
    #   "row_number": 3,
    #   "col_number": 2
    # }))

    # print(solve_part1({
    #   "flow_rate": 20,
    #   "time": 40,
    #   "row_number": 3,
    #   "col_number": 1
    # }))

    # print(solve_part2({
    #   "flow_rate": 20,
    #   "amount_of_soup": 87.5,
    #   "row_number": 3,
    #   "col_number": 1
    # }))

    #  print(solve_part3({
    #   "flow_rate": 20,
    #   "time": 7.5,
    #   "row_number": 0,
    #   "col_number": 0
    # }))
    print(solve_part3({
      "flow_rate": 20,
      "time": 8,
      "row_number": 1,
      "col_number": 0
    }))

    print(solve_part3({
      "flow_rate": 20,
      "time": 8,
      "row_number": 1,
      "col_number": 1
    }))

