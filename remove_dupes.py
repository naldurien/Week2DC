def remove_dupes():

    emails = open('random_gen_emails.txt', 'r').read()
    #listify the data with .split()
    emails = emails.split()
    de_duped = []
    for email in emails:
        if email not in de_duped:
            de_duped.append(email)
    return de_duped 
    emails.close()

de_duped_emails = open('duplicate_free_email_list.txt', 'w')

for email in remove_dupes():
    email = email.strip(',')
    de_duped_emails.write(f"{email} \n")

de_duped_emails.close()

remove_dupes()
