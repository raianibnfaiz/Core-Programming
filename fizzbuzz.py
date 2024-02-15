#https://leetcode.com/problems/fizz-buzz/
n = 15
a = []
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        my_string = '"' + "FizzBuzz" + '"'
        a.append(my_string)
        print('FizzBuzz')
    elif i % 3 == 0:
        my_string = '"' + "Fizz" + '"'
        a.append(my_string)
        print('Fizz')
    elif i % 5 == 0:
        my_string = '"' + "Buzz" + '"'
        a.append(my_string)
        print('Buzz')
    else:
        my_string = '"' + str(i) + '"'
        a.append(str(my_string))  # Convert integer to string
        print(i)
for i in a:
    print(i, end=",")
