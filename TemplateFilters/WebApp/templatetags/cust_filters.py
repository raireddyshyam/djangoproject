from django import template

register = template.Library()

def five(value,n):
    result=value[0:n]
    return result
register.filter('cn',five)