# WK 2 DAY 3 ACTIVITY
# Write to file.

f = open("guest.txt", "a")
name = input("Please enter your name: ") + ", "
f.write(name)
f.close()

while True:
    user_reason = input("Why do you like programming? (Press q if you want to quit.): ")  
    reason = '"' + user_reason + '", 
    f = open("reasons.txt", "a")
    if user_reason == "q":
        f.close()
        exit()
    else:
        f.write(reason)

