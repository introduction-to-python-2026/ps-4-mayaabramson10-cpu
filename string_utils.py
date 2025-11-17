def split_at_first_digit(formula):
    n = []
    n_num = 0
    for i in range(len(formula)):
        if formula[i].isdigit() == true:
            n.append(i)
            n_num =+1
    w = ""
    if n_num == 0:
        return (formula, 1)
    for i in range(n.lenght):
        w = w + (formula[w:i])
    print(w)
        

def split_before_each_uppercases(formula):
    y = []
    y_num = 0
    for i in range(len(formula)):
        if formula[i].isupper() == true:
            y.append(i)
            y_num =+1
    g = ""
    if y_num == 0:
        return formula
    for i in range(y.lenght):
        g = g + (formula[g:i])
    print (g)
        
    
 

