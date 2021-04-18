num1=75
num2=51
num3=119
if num1>=num2 or num3>=num1:
    print("is greater" )
    if num2<=num3 or num2<=num1:
        print("is less")
        if num3>>num1 or num3>>num2:
            print("more greater")
        else:
            print("is less")
    else:
        print("is greater")
else:
    print("is more greater")

# n1=119
# n2=75
# n3=30
# if n1>=n2 or n1>=n3:
#     print("is more greater")
#     if n2>=n1 or n1>=n2: 
#         print("is greater")
#         if n3<=n2 or n3<=n1:
#             print("is less")
#         else:
#             print("is greater")
#     else:
#         print("is more greater")
# else:
#     print("is less")