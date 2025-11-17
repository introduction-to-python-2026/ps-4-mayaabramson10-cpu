def split_at_first_digit(formula):
    n = []
    n_num = 0
    for i in range(len(formula)):
        if formula[i].isdigit() == true:
            n.append(i)
            n_num =+1
    w = 0
    if n_num == 0:
        return (formula, 1)
    for i in range(len(n)):
        print formula[w:i]
        w =+1

def split_before_each_uppercases(formula):
    y = []
    y_num = 0
    for i in range(len(formula)):
        if formula[i].isupper() == true:
            y.append(i)
            y_num =+1
    g = 0
    if y_num == 0:
        return formula
    for i in range(len(y)):
        print formula[g:i]
        g = g+1
    
 

