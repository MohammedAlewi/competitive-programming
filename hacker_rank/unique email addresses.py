def format_email(email):
    email=list(email)

    remove=False
    for i in range(len(email)):
        if email[i]=='@':
            break
        
        if email[i]=='+':
            remove=True

        if email[i]=='.':
            email[i]=''

        if remove:
            email[i]=''

    return "".join(email)


def unique_email_address(emails):
    uinque=set()

    for email in emails:
        em= format_email(email)
        uinque.add(em)

    return len(uinque)

print( unique_email_address(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]) )