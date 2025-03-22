with open('constructor.py','r') as file:
    print(file.read())
    file.close()

with open('test.xml','w') as write_file:
    write_file.write('hello')
    write_file.close()

with open('test.xml','r+') as read_write:
    read_write.write("Hello there!")
    read_write.close()
