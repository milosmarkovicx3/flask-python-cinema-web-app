import re
from flask import jsonify

def json(entity):
    return jsonify(entity.__repr__())

def email_regex(value):
    email_regex = r'^(?=.{1,255}$)\w+(\w|((?<!\.)\.))*\w+\@\w+(\w|((?<!\.)\.))*\.\w{2,4}$'
    return re.search(email_regex, value)

def passwd_regex(value):
    passwd_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W]).{5,50}$'
    return re.search(passwd_regex, value)

def basic_regex(value):
    basic_regex = r'^(?=.{1,255}$)\w{2,}'
    return re.search(basic_regex, value)