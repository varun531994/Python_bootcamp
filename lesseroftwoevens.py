def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        result = min(a,b)
        
    else:
        result = max(a,b)
    
    return result