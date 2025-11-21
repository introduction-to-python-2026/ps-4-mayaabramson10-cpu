def split_at_digit(formula):
    first_digit_index = -1
    
    for i, char in enumerate(formula):
        if char.isdigit():
            first_digit_index = i
            break
            
    if first_digit_index == -1:
        return (formula, 1)
        
    prefix = formula[:first_digit_index]
    number_str = formula[first_digit_index:]
    number = int(number_str)
    
    return (prefix, number)


def split_before_each_uppercase(formula):
    segments = []
    current_segment_start_index = 0
    
    if not formula:
        return []

    for i in range(1, len(formula)):
        char = formula[i]
        
        if char.isupper():
            segment = formula[current_segment_start_index:i]
            segments.append(segment)
            
            current_segment_start_index = i
            
    last_segment = formula[current_segment_start_index:]
    segments.append(last_segment)
    
    return segments
