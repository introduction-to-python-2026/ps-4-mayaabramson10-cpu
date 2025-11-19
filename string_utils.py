def split_at_first_digit(formula):
  for i in range(len(formula)):
    if formula[i].isdigit():
      return formula[:i] , int(formula[i:])
      break
  return formula, 1

def split_before_each_uppercases(formula):
    start = 0
  list = []
for i in range(1, len(formula)):
  if formula[i].isupper():
    list.append(formula[start:i])
    start = i
list.append(formula[start:])
return list
                
      
   
    
    
 

