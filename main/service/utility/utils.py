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

def repr_helper_method(root):
    """
    Kada treba da se dobije __repr__() objekata u listi.
    :param root: Bilo koja potencijalna lista objekata.
    :return: Listu rečnika koji predstavljaju konvertovane objekte.
    """
    if not isinstance(root, list):
        return root.__repr__()
    _list = []
    for item in root:
        if isinstance(item, list):
            _sub_list = repr_helper_method(item)
            _list.append(_sub_list)
        else:
            _list.append(item.__repr__())
    return _list