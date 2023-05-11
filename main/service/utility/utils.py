import re


def email_regex(value):
    regex = r'^(?=.{1,255}$)\w+(\w|((?<!\.)\.))*\w+\@\w+(\w|((?<!\.)\.))*\.\w{2,4}$'
    return re.search(regex, value)

def passwd_regex(value):
    regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W]).{5,50}$'
    return re.search(regex, value)

def basic_regex(value):
    regex = r'^(?=.{1,255}$)\w{2,}'
    return re.search(regex, value)

