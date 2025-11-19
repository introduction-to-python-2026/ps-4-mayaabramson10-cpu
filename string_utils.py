def split_at_first_digit(formula):
  digit_place = []
  for i in range(len(formula)):
    if formula[i].isdigit() == True:
      digit_place.append(i)
  result = []
  if len(digit_place) == 0:
    result.append(formula)
    result.append(1)
    return (result)
  else:
    result.append(formula[:digit_place[0]])
    result.append(formula[digit_place[0]:])
    return (result)
    

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
    
    
 

