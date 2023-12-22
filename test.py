import string

chars = list(string.ascii_uppercase)

# for char in chars : 
#         for num in range(1,3001):
#                 path = "docs/{}/{}{}".format(char,char,num)
#                 print(path)

                
table = dict(zip(string.ascii_uppercase,range(1,27)))
# print(table.get('A'))

def printer(char) : 
        print([table.get(char),0,0])
        

for x in chars :
        printer(x)