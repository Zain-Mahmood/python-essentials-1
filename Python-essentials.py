x = input("number of employees ")

first_names = []
last_names = []
age = []

for i in range(int(x)):
        a = input("First name ")
        while a == "":
            a = input("First name ")
            if a == "":
                continue
            else: break
        
        first_names.append(a)
        
        b = input("Last name ")
        while b == "":
            b = input("Last name ")
            if b == "":
                continue
            else: break
        
        last_names.append(b)
        
        c = input("Age ")
        while 18 > int(c) or int(c)> 100:
            c = input("Age ")
            if 18 > int(c) or int(c) > 100:
                continue
            else: break
        
        age.append(int(c))
        
        
        
print(first_names)
print(last_names)
print(age)


sum_of_ages = sum(age)
if sum_of_ages > 500:
    print("Sum of employee ages is over 500")
print(sum_of_ages)
