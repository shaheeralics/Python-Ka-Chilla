                                            # check whether the person is eligible to CSS Test

max_age=30
your_name=input("Enter your Name :")
your_age=input("Enter your age : ")
your_age=int(your_age)
if your_age > max_age:
    print (your_name," You are not eligible for CSS test")
elif your_age <= 24:
    print(your_name," You are not eligible for CSS Test")
else:
    print(your_name," You can take CSS Test")
    