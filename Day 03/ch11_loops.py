                                #there are two types of loops in python

                                        # 1.for loop 2.while loop
# # while loop
# x=1
# while (x<=5):
#     print(x)
#     x=x+1
    
# # for loop
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
# print(fruit)


# for y in range(13,19):
#     print(y)

                                # how to implement the for loop in program

# days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# for d in days:
#     # if (d=="Friday"):break  #ends the loop when friday comes
#     if (d=="Friday"):continue #skips Friday
#     print(d)
    
# nested loop

outer_list=[10,20,30]
inner_list=['a','b','c']

for o in outer_list:
    for i in inner_list:
        print(i,'=',o)   
 
        