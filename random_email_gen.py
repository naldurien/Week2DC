import random

domains = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@emoryhealthcare.org', '@txstate.edu', '@rit.edu', '@austincc.edu', '@wustl.edu']


def random_email():
    rand_domain = random.choice(domains)
    rand_id = ""
    rand_id = ''.join(random.choice('abcedefghijklmnopqrstuvwxyz') for i in range(random.randint(4, 8)))
    email = rand_id + rand_domain
    return email

def self_gen_emails():
    email_list = []
    i = 0
    while i < 50:
        email_list.append(random_email())
        i +=1
        if i % 13  == 0:
            double = random_email()
            email_list.append(double)
            email_list.append(double)
    random_gen_emails = open('random_gen_emails.txt', 'w')
    for email in email_list:
        email = email.strip(',')
        random_gen_emails.write(f"{email} \n")
    random_gen_emails.close()

self_gen_emails()
