print("I am learing functions")
print("I am learing functions")
print("I am learing functions")
print("I am learing functions")
print("I am learing functions")
print("I am learing functions")
print("I am learing functions")

                                    # defining a function
                                    



def print_codamics():
    print("I am learing functions")
    print("I am learing functions")
    print("I am learing functions")

print_codamics()

                                    # no_2 method to define a function
                                    
def print_codamics():
    text="Subscribe to my youtube channel 'Tech Wali Tricks' "   # we can correct all the spelling Mistakes at ones
    print(text)
    print(text)
    print(text)
print_codamics()

                                #    3rd way of defining a function

def print_codamics(text):
    print(text)
    print(text)
    print(text)

print_codamics("I am learning python with Dr. Aammar in Codanics.com website")

def CSS_eligibility_Calculator(your_name=input("Enter your name : "),your_age=input("Enter your age : "),min_age=24,max_age=30):
    your_age=int(your_age)
    if your_age > max_age:
        print (your_name," You are not eligible for CSS test")
    elif your_age < min_age:
        print(your_name," You are not eligible for CSS Test")
    else:
        print(your_name," You can take CSS Test")
        
CSS_eligibility_Calculator()

                                    # Defining a function of Future
                                    
def future_age(age):
    new_age=age+20
    return new_age
    # print(new_age)     #isko direct bhi kar sakte hai lekin Dr.Aammar ne long method chose k
                            # iya hai is lia nahi kiya mene
 
future_predicted_age=future_age(35)
print(future_predicted_age)
