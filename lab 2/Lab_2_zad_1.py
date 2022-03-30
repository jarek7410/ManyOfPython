
text=""
for i in range(504,3001,7):
    if(i%5==0):
        text=text+str(i)
print(text)
#for i in range(text.count("21")):
 #   k=text.find("21")
  #  text[k:k+1]="XX"
print(text.count("21"))
text=text.replace("21","XX")

print(text)