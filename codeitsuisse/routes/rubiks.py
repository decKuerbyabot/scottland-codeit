def RubiksCube(ops,state):
    operation = [*ops]
    u = state["u"]
    l = state["l"]
    f = state["f"]
    r = state["r"]
    b = state["b"]
    d = state["d"]
    def U():
        temp1 = l[0]  
        l[0] = f[0]
        f[0] = r[0]
        r[0] = b[0]
        b[0] = temp1

    def Ui():
        temp2 = l[0]  
        l[0] = b[0]
        b[0] = r[0]
        r[0] = f[0]
        f[0] = temp2

    def D():
        temp3 = l[2]  
        l[2] = b[2]
        b[2] = r[2]
        r[2] = f[2]
        f[2] = temp3

    def Di():
        temp4 = l[2]  
        l[2] = f[2]
        f[2] = r[2]
        r[2] = b[2]
        b[2] = temp4

    def L():
        temp5 = [u[0][0],u[1][0],u[2][0]]
        u[0][0] = b[0][0]
        u[1][0] = b[1][0]
        u[2][0] = b[2][0]
        b[0][0] = d[0][0]
        b[1][0] = d[1][0]
        b[2][0] = d[2][0]
        d[0][0] = f[0][0]
        d[1][0] = f[1][0]
        d[2][0] = f[2][0]
        f[0][0] = temp5[0]
        f[1][0] = temp5[1]
        f[2][0] = temp5[2]
        
        

    def Li():
        temp6 = [u[0][0],u[1][0],u[2][0]]
        u[0][0] = f[0][0]
        u[1][0] = f[1][0]
        u[2][0] = f[2][0]
        f[0][0] = d[0][0]
        f[1][0] = d[1][0]
        f[2][0] = d[2][0]
        d[0][0] = b[0][0]
        d[1][0] = b[1][0]
        d[2][0] = b[2][0]
        b[0][0] = temp6[0]
        b[1][0] = temp6[1]
        b[2][0] = temp6[2]
        
    def R():
        temp7 = [u[0][0],u[1][0],u[2][0]]
        u[0][2] = f[0][2]
        u[1][2] = f[1][2]
        u[2][2] = f[2][2]
        f[0][2] = d[0][2]
        f[1][2] = d[1][2]
        f[2][2] = d[2][2]
        d[0][2] = b[0][2]
        d[1][2] = b[1][2]
        d[2][2] = b[2][2]
        b[0][2] = temp7[0]
        b[1][2] = temp7[1]
        b[2][2] = temp7[2]

    def Ri():
        temp8 = [u[0][0],u[1][0],u[2][0]]
        u[0][2] = b[0][2]
        u[1][2] = b[1][2]
        u[2][2] = b[2][2]
        b[0][2] = d[0][2]
        b[1][2] = d[1][2]
        b[2][2] = d[2][2]
        d[0][2] = f[0][2]
        d[1][2] = f[1][2]
        d[2][2] = f[2][2]
        f[0][2] = temp8[0]
        f[1][2] = temp8[1]
        f[2][2] = temp8[2]
           

    def F():
        temp9 = [l[0][2],l[1][2],l[2][2]]  
        l[0][2] = d[2][0]
        l[1][2] = d[2][1]
        l[2][2] = d[2][2]
        d[2][0] = r[0][0]
        d[2][1] = r[1][0]
        d[2][2] = r[2][0]
        r[0][0] = u[2][0]
        r[1][0] = u[2][1]
        r[2][0] = u[2][2]
        u[2][0] = temp9[2]
        u[2][1] = temp9[1]
        u[2][2] = temp9[0]
        
        

    def Fi():
        temp10 = [l[0][2],l[1][2],l[2][2]]  
        l[0][2] = u[2][0]
        l[1][2] = u[2][1]
        l[2][2] = u[2][2]
        u[2][0] = r[0][0]
        u[2][1] = r[1][0]
        u[2][2] = r[2][0]
        r[0][0] = d[2][0]
        r[1][0] = d[2][1]
        r[2][0] = d[2][2]
        d[2][0] = temp10[0]
        d[2][1] = temp10[1]
        d[2][2] = temp10[2]

    def B():
        temp11 = [l[0][0],l[1][0],l[2][0]]  
        l[0][0] = u[0][0]
        l[1][0] = u[0][1]
        l[2][0] = u[0][2]
        u[0][0] = r[0][2]
        u[0][1] = r[1][2]
        u[0][2] = r[2][2]
        r[0][2] = d[0][0]
        r[1][2] = d[0][1]
        r[2][2] = d[0][2]
        d[0][0] = temp11[0]
        d[0][1] = temp11[1]
        d[0][2] = temp11[2]

    def Bi():
        temp12 = [l[0][2],l[1][2],l[2][2]]  
        l[0][0] = d[0][0]
        l[1][0] = d[0][1]
        l[2][0] = d[0][2]
        d[0][0] = r[0][2]
        d[0][1] = r[1][2]
        d[0][2] = r[2][2]
        r[0][2] = u[0][0]
        r[1][2] = u[0][1]
        r[2][2] = u[0][2]
        u[0][0] = temp12[2]
        u[0][1] = temp12[1]
        u[0][2] = temp12[0]
        

    for i in range(len(operation)):
        if (i != (len(operation)-1)):    
            if (operation[i] == 'U'):
                if (operation[i+1] == 'i'):
                    Ui()
                    i+=1
                else:
                    U()
            elif (operation[i] == 'D'):
                if (operation[i+1] == 'i'):
                    Di()
                    i+=1
                else:
                    D()
            elif (operation[i] == 'L'):
                if (operation[i+1] == 'i'):
                    Li()
                    i+=1
                else:
                    L()
            elif (operation[i] == 'R'):
                if (operation[i+1] == 'i'):
                    Ri()
                    i+=1
                else:
                    R()
            elif (operation[i] == 'F'):
                if (operation[i+1] == 'i'):
                    Fi()
                    i+=1
                else:
                    F()
            elif (operation[i] == 'B'):
                if (operation[i+1] == 'i'):
                    Bi()
                    i+=1
                else:
                    B()
        else:
            if (operation[i] == 'i'):
                pass
            elif (operation[i] == 'U'):
                U()
            elif (operation[i] == 'D'):
                D()
            elif (operation[i] == 'L'):
                L()
            elif (operation[i] == 'R'):
                R()
            elif (operation[i] == 'F'):
                F()
            elif (operation[i] == 'B'):
                B()
    #print(u,l,f,r,b,d)
    dict={"u": u, "l": l, "f": f, "r": r, "b": b, "d": d}
    return dict
