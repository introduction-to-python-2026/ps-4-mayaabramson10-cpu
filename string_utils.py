def split_at_first_digit(formula):
    i = 0
    while i < len(formula) and not formula[i].isdigit():
      i += 1
    
    if i == len(formula):
      return (formula, 1)
        
    prefix = formula[:i]
    number = int(formula[i:])
    
    return (prefix, number)

def split_before_each_uppercase(formula):
    segments = []
    start = 0
    
    for i in range(1, len(formula)):
      if formula[i].isupper():
        segments.append(formula[start:i])
        start = i
            
    segments.append(formula[start:])
    
    return segments


