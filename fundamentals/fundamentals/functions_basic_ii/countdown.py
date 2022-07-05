def countdown(number):
    countdown_list = []
    for x in range(number, -1, -1):
        countdown_list.append(x)
    return(countdown_list)

print(countdown(5))