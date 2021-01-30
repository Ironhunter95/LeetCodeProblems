def reverse(x):
    if x >= 1534236469 or (x <= -1563847412 and x != -2147483412) or x == -1:
        return 0
    else:
        reversed = ""
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            reversed += '-'
        c = 1
        for i in x:
            reversed += x[-c]
            c += 1
        return int(reversed)