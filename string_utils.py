def split_at_first_digit(formula):
  digit_place = [0]
  digit_num = 0
  for index in range(len(formula)):
    if formula[index].isdigit()== True:
      digit_place.append(index)
      digit_num =+1
  
  if digit_num != 0:
      resoult = ""
      for place in range(len(digit_place)):
        if place + 1 < len(digit_place):
          resoult = resoult + " " + str(formula[digit_place[place]:digit_place[place+1]])
        else:
          resoult = resoult + " " + str(formula[digit_place[place]:])
      print (resoult)
  else:
    print (formula , 1) 

  


def split_before_each_uppercases(formula):
    upper_place = [0]
    upper_num = 0
    for i in range(len(formula)):
        if formula[i].isupper() == True:
            upper_place.append(i)
            upper_num =+1
    
    if upper_num != 0:
      k = ""
      for g in range(len(upper_place)):
        if g+1 < len(upper_place):
          k = k + " " + str(formula[upper_place[g]:upper_place[g +1]])
        else:
          k = k + " " + str(formula[upper_place[g]:])
      print(k)
    else:
      print(formula)

    
    
 

