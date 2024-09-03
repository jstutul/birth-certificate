alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

text=str(input("Enter your text :")).upper()
key=int(input("Enter Key value :"))
result=""
for i in text:
    if i in alphabets:  
        position = alphabets.index(i)
        shifted_position = (position + key) % 26 
        result+=alphabets[shifted_position]
    else:
        result+=""
print(result)

dresult=""
for i in result:
    position = alphabets.index(i)
    shifted_position = (position - key) % 26 
    dresult+=alphabets[shifted_position]
print(dresult)