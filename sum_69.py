def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
    

arr = [1,2,3,4,5,6,7,8,9]

z = int(input('Enter 1'))

if z == 1:
 print(summer_69(arr))
else:
 pass