    # logical operators are either "True" or "False", "0" or "1"
# equal to ==
# less than  <
# greater than >
# less than and equal to <=
# greater than and equal to >=

# print(4==4)     # when use = then we have to use == in python , otherwise its a syntax error
# print(3<5)      # True
# print(2>7)      # False
# print(6<=8)     # True  
# print(9>=2)     # True
# # not operator is used for reversing the boolean value of expression
# print(not (3<5))    # False because it will return opposite of what's inside brackets
# print((3>5)!=True)  # True

# bitwise operators
# & : AND Operator
# |: OR Operator
# ^: XOR Operator
# ~: NOT Operator
# <<: Left shift Operator
# >>: Right Arithmetic Shift Operator
# >>>: Right Logical Shift Operator
# a=5
# b=3
# c=(a&b)
# d=(a|b)
# e=(a^b)
# f=(~a)
# g=(a<<2)
# h=(a>>2)
# print("Bitwise AND Operation Result: ", c)
# print("Bitwise OR Operation Result: ", d)

                                        
                                        #applications of logical operators

sikandar_age=input("Enter Age of Sikandar : ")
print(type(sikandar_age))
sikandar_age=int(sikandar_age)          #convert input string to integer
# print(type(sikandar_age))
age_at_school=5
print(sikandar_age >= age_at_school)