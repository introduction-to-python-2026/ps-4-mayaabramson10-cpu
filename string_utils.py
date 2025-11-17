
def split_at_first_digit(formula):
    n = -1
    for i in range(len(formula)):
        if formula[i].isdigit() == true:
            n = i
            break
    if n == -1:
        return (formula, 1)
    m =formula(:n)
    l =formula(n:)
    return (m, l)

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
    
 
