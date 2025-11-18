def split_at_first_digit(formula):
  digit_place = [0]
  digit_num = 0
  for index in range(len(formula)):
    if formula[index].isdigit()== True:
      digit_place.append(index)
      digit_num += 1
  resoult = []
  if digit_num != 0:
    resoult.append(formula[:digit_place[1]])
  else:
    resoult.append(formula, 1)
  print (resoult)
      


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
      
    print(k)
    
    
 

