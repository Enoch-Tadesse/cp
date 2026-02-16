def is_taxi(number):
    digits = number.replace("-", "")
    return all(d == digits[0] for d in digits)

def is_pizza(number):
    digits = number.replace("-", "")
    return all(digits[i] > digits[i+1] for i in range(5))

n = int(input())
friends = []

for _ in range(n):
    s, name = input().split()
    s = int(s)
    taxi = pizza = girl = 0

    for _ in range(s):
        num = input()
        if is_taxi(num):
            taxi += 1
        elif is_pizza(num):
            pizza += 1
        else:
            girl += 1

    friends.append((name, taxi, pizza, girl))

max_taxi = max(f[1] for f in friends)
max_pizza = max(f[2] for f in friends)
max_girl = max(f[3] for f in friends)

taxi_names = [f[0] for f in friends if f[1] == max_taxi]
pizza_names = [f[0] for f in friends if f[2] == max_pizza]
girl_names = [f[0] for f in friends if f[3] == max_girl]

print("If you want to call a taxi, you should call: " + ", ".join(taxi_names) + ".")
print("If you want to order a pizza, you should call: " + ", ".join(pizza_names) + ".")
print("If you want to go to a cafe with a wonderful girl, you should call: " + ", ".join(girl_names) + ".")
