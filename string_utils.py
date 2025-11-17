def split_before_each_uppercases(formula):
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


def split_at_first_digit(formula):
    y = -1
    for i in range(len(formula)):
        if formula[i].isupper() == true:
            y= i
            break
    if y == -1:
        return (formula)
    u = formula(:y)
    t = formuls(y:)
    return (u,t)
