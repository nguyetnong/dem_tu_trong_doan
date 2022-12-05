

text=input("nhap doan van bat ki:")
text_split=text.split()

dict_value={}
    
for item in text_split:
    if item in dict_value:
        dict_value[item]=int(dict_value[item])+1
    else:
        dict_value[item]=1
print(dict_value)