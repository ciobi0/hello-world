# assume that an empty string isn't a palindrome; kayak kayak cuuc
text = input("introdu palindrome: ")
# treat upper- and lower-case letters as equal;
text = text.upper()
# spaces are not taken into account during the check – treat them as non-existent;
text = text.replace(' ', '')
# there are more than a few correct solutions – try to find more than one.
mijloc = int(len(text)/2)
jumate1 = text[:mijloc]
jumate2 = text[mijloc+1:]
jumate3=[]
for ch in jumate2:
    jumate3.insert(0,ch)
jumate4 = "".join(jumate3)

if(jumate1 == jumate4):
    print("este palindrome")
else:
    print("nu este palindrome")

