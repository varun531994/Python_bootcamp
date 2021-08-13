#Fun Problem:

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


x = input('Enter your letter:a/b/c/d/e:')

if x == 'a':
 print(print_big(x))
 
elif x =='b':
 print(print_big(x))

elif x == 'c':
 print(print_big(x))
elif x == 'd':
 print(print_big(x))
elif x == 'e':
 print(print_big(x))
else:
 pass
 
  