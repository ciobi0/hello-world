# asks the user for two separate texts;
input1 = input('scrie primul cuvant: ')
input2 = input('scrie al doilea cuvant: ')

# treat upper- and lower-case letters as equal;
input1 = input1.lower()
input2 = input2.lower()
# spaces are not taken into account during the check – treat them as non-existent
input1 = input1.replace(' ', '')
input2 = input2.replace(' ', '')
# assume that two empty strings are not anagrams;
if len(input1)==0 or len(input2) == 0:
    print('nu sunt anagrame sirurile goale')
# checks whether, the entered texts are anagrams and prints the result.
if(len(input1) != len(input2)):
    print('nu sunt anagrame cele doua siruri')
else:
    c =''
    for ch in input1:
        if ch not in input2:
           c = 'nu sunt anagrame'
           break
        else:
            c = 'sunt anagrame'
    print (c)

# better solution
# str_1 = input("Enter the first string: ")
# str_2 = input("Enter the second string: ")

# strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
# strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
# if len(strx_1) > 0 and strx_1 == strx_2:
# 	print("Anagrams")
# else:
# 	print("Not anagrams")

