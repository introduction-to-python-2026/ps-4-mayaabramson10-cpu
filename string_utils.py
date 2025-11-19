def split_at_first_digit(formula):
  for i in range(len(formula)):
    if formula[i].isdigit():
      return formula[:i] , int(formula[i:])
  return formula, 1

def split_before_each_uppercases(formula):
    upper_place = []
    upper_num = 0
    for i in range(len(formula)):
        if formula[i].isupper() == True:
            upper_place.append(i)
            upper_num += 1
    
    if upper_num != 0:
      k = []
      for g in range(len(upper_place)):
        if g+1 < len(upper_place):
          k.append(formula[upper_place[g]:upper_place[g + 1]])
        else:
          k.append(formula[upper_place[g]:])
      
    else:
      k.append(formula)
      
    return(k)
    
    
 

