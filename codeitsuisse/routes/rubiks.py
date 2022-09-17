def rotate(matrix):
    n = 3
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp
    print(matrix)

def reverse(matrix):
    n = 3
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[i][j]
            matrix[i][j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = tmp

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
        rotate(u)

    def Ui():
        temp2 = l[0]  
        l[0] = b[0]
        b[0] = r[0]
        r[0] = f[0]
        f[0] = temp2
        reverse(u)

    def D():
        temp3 = l[2]  
        l[2] = b[2]
        b[2] = r[2]
        r[2] = f[2]
        f[2] = temp3
        rotate(d)

    def Di():
        temp4 = l[2]  
        l[2] = f[2]
        f[2] = r[2]
        r[2] = b[2]
        b[2] = temp4
        reverse(d)

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
        rotate(l)
        
        

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
        reverse(l)
        
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
        rotate(r)

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
        reverse(r)
           

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
        rotate(f)
        
        

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
        reverse(f)

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
        rotate(b)

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
        reverse(b)

    oper_dict = {'U': U, 'L': L, 'D': D, 'B': B, 'F': F, 'R': R, 'Ui': Ui, 'Li': Li, 'Di': Di, 'Bi': Bi, 'Fi': Fi, 'Ri': Ri}
    i = 0
    while(i < len(operation)):
        if i+1 < len(operation) and operation[i+1] == 'i':
            if i + 2 < len(operation) and operation[i + 2] == operation[i]:
                i += 3
                continue
            oper_dict["".join(operation[i:i+2])]()
            i += 2
        elif i+2 < len(operation) and operation[i+1] == operation[i] and operation[i+2] == "i":
            i += 3
        else:
            print(i, operation[i])
            oper_dict[operation[i]]()
            i += 1

    dicts = {"u": u, "l": l, "f": f, "r": r, "b": b, "d": d}
    return dicts
