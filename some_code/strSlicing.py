fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])
#both are same
print("both are same")
print(fruit[0:-3])
print(fruit[:len(fruit)-3])

# down three are same
print("down three are same")
print(fruit[len(fruit)-1:len(fruit) - 3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-1:- 3])


print(fruit[-3:-1])

# Quick Quiz:
nm = "Harry"
print(nm[-4:-2])


#output
# 5
# mang
# ang
# Mang
# Ma
# Ma
# Error
# Error
# Error
# ng


#Quick Quiz
# ar
