a = input("Enter the expression: ")
lst = []

for i in a:
    lst.append(i)

print(lst)


# first we will solve for '*' and '/'
i = 0
while i < len(lst):
    if lst[i] == "/" or lst[i] == "*":
        s = i
        x = float(lst[s-1])
        y = float(lst[s+1])

        if lst[i] == "/":
            c = x / y
        else:
            c = x * y

        # print(c)

        lst.pop(s-1)
        lst.pop(s-1)
        lst.pop(s-1)
        lst.insert(s-1, c)

        # print(lst)
        i = 0   # restart scan after change
    else:
        i += 1


#now solve for "+" and "-"
i = 0
while len(lst) > 1:
    if lst[i] == "+" or lst[i] == "-":
        s = i
        x = float(lst[s-1])
        y = float(lst[s+1])

        if lst[i] == "+":
            c = x + y
        else:
            c = x - y

        # print(c)

        lst.pop(s-1)
        lst.pop(s-1)
        lst.pop(s-1)
        lst.insert(s-1, c)

        # print(lst)
        i = 0
    else:
        i += 1


print("Final answer:", lst[0])





