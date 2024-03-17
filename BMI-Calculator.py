#!/usr/bin/env python
# coding: utf-8

# In[10]:


name = input("Enter your name: ")

Weight = int(input("Enter your weight in pounds: "))

Height = int(input("Enter your height in inches: "))

BMI = (Weight*703)/(Height * Height)

print(BMI)

if BMI>0:
    if(BMI<18.5):
        print(name+", you are underweight.")
    elif(BMI<=24.9):
        print(name+", you are normal weight.")
    elif(BMI<=29.9):
        print(name+", you are overweight.")
    elif(BMI<=34.9):
        print(name+", you are obese.")
    elif(BMI<=39.9):
        print(name+", you are severelt obese.")
    else:
        print(name+", you are morbidly obese.")
else:
    print("Enter valid input")


# In[ ]:


#BMI = (Weight in pounds x 703)/(Height * height in inches)


# In[ ]:


# Under 18.5 - UnderWeightMinimal
# 18.5 - 24.9 - Normal Weight - Minimal
# 25 - 29.9 - Overweight - Increased
# 30 - 34.9 - Obese - High
# 35 - 39.9 - Severely Obese - Very High
# 40 and over - Morbidly Obese - Extremely High


# In[9]:


# if BMI>0:
#     if(BMI<18.5):
#         print(name+", you are underweight.")
#     elif(BMI<=24.9):
#         print(name+", you are normal weight.")
#     elif(BMI<=29.9):
#         print(name+", you are overweight.")
#     elif(BMI<=34.9):
#         print(name+", you are obese.")
#     elif(BMI<=39.9):
#         print(name+", you are severelt obese.")
#     else:
#         print(name+", you are morbidly obese.")
# else:
#     print("Enter valid input")


# In[ ]:





# In[ ]:





# In[ ]:




