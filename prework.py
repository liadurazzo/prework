#question 1
def hello_name(user_name):   
    print(f'Hello {user_name}!')

hello_name('lia')


#question 2  
def first_odds():
    for num in range (101):
        if not num % 2 :
            print(num) 

first_odds()

#question3 
def max_num_in_list(a_list):
    result = max(a_list)
    print(result)
lia_list = [1 , 24, 13, 4, 75, 6, 47, 30, 25, 55,]
max_num_in_list(lia_list)

#question 4 
def is_leap_year(a_year):
    test = (a_year % 4 == 0 and a_year % 100 != 0) or a_year % 400 == 0
    if test : 
        print(f" {a_year} is a leap year .")
    else:
        print(f" {a_year} is not a leap year.")
is_leap_year(2024)

#question 5
def is_consecutive(a_list):
    
     return all (a_list[i + 1] - a_list[i] == 1 for i in range(len(a_list) - 1))
print(is_consecutive([1, 2, 4, 5]))


