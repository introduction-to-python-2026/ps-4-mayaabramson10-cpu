def split_at_first_digit(formula):
  digit_place = [0]
  digit_num = 0
  for i in range(len(formula)):
    if formula[i].isdigit()== True:
      digit_place.append(i)
      digit_num =+1
  
  if digit_num != 0:
      resoult = ""
      for place in range(len(digit_place)):
        if place + 1 < len(formula):
          resoult = resoult + " " + (formula[digit_place[place]:digit_place[place+1]])
        else:
          resoult = resoult + " " + (formula[digit_place[place]:])
      print (resoult)
  else:
    print (formula , 1) 

  


def split_before_each_uppercases(formula):
    upper_place = [0]
    upper_num = 0
    for i in range(len(formula)):
        if formula[i].isupper() == true:
            upper_place.append(i)
            upper_num =+1
    
    if upper_num != 0:
      k = ""
      for i in range(len(upper_place)):
        if i+1 < len(formula):
          k = k + " " + (formula[upper_place[i]:upper_place[i+1]])
        else:
          k = k + " " + (formula[upper_place[i]:])
      print(k)
    else:
      print(formula)
        
    
        
    
 

