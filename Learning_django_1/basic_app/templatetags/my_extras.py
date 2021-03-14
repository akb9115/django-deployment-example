from django import template

register = template.Library()

# @register.filter(name='myTrimFunc')
def myCustomCapitalization(value,index):
    """
    This cuts out all values of "arg" from the string
    """
    split_s = list(value)
    split_s[index] = split_s[index].upper()
    return "".join(split_s)


register.filter('myCustomCapitalization',myCustomCapitalization)