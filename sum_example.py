#adds the sum of the number while counting down
def sum(num):
    result = 0
    for i in range(num):
        result = result + num-i

    print(result) 



sum(5)