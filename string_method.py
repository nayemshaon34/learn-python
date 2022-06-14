course = "Theory of Computation"
print(len(course))  #len of a string
# here len and print are general purpose functions , they don't belong to number, string or any kinds of objects
print(course.upper()) # this upper function is more specific to string, so we call this as method
print(course.lower())
print(course.title()) #Return a version of the string where each word is titlecased.
print(course.find('o')) #return the index of the letter or words where it has started and it's case sensitive
print(course.find('Computation'))

print(course.replace('of','Off')) #case sensitive
print('THeory' in course) # is the word THeroy available in course ? // will return boolean value
