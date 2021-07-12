import re

dict_email = {}


def email_parse(email):
    SPLIT_EMAIL = re.split(r'@', email)
    PARSER_USERNAME = re.compile(r'^[0-9A-Za-z]')
    PARSER_DOMAIN = re.compile(r'^[a-z]+\.[a-z]+')
    if PARSER_USERNAME.findall(SPLIT_EMAIL[0]) and PARSER_DOMAIN.findall(SPLIT_EMAIL[1]):
        dict_email['username'] = SPLIT_EMAIL[0]
        dict_email['domain'] = SPLIT_EMAIL[1]
    if not dict_email:
        raise ValueError(f'wrong email: {email}')
    print(dict_email)


email_parse("email14@gmail.com")
