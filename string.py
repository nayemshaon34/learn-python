course = "hello , are u deaf&@"
ano = course [:]
courses = '''
    How you doing?
    i was writing you a letter
    hope you are fine
    thank you so much 
    
    yours ever
    Nayem
    
''' #for writing multiline string
print(courses)

print("index value is " +course[4])
print("index value is " +course[-1]) #index of the last character
print("index value is " +course[-2]) #will retrun second character from the end
print(course[0:3]) #will print from 0 index to 2 no index and exclude the no 3 index
print(course[3:]) #will print from 3 no index to the end of the string
print(course[:]) #will print from 0 no of index to the end
print(ano) #copy the whole string into ano string
