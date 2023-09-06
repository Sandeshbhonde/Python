# Write a program to print "Yeah" if string contains vowels otherwise print "Nooo".
# Take string1 = "Hello Apple" string2 = "Cry Fry Dry"

string = input ("Enter a string : ")

vowels = {'a','e','i','o','u'}

i = 0
vowels_present = False
 
for i in string:
    if i.lower() in vowels:
        vowels_present = True
        break

if vowels_present :
    print("Yess !")

else:
    print("Nooo.!")
    
    
    
    

