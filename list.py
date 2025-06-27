with open('myfile.txt','w') as file:
    file.write('this is my first file program,\nwhen i tried to diectly read\nan already existing file it removed all of its \ncontent for some reason unknown to me')
with open('myfile.txt','r') as file:
    content=file.readlines()
    content=[line.strip() for line in content]
    print(content)
    
