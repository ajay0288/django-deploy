from django import forms


def startswitha(value):
    if value[0] != 'a':
        raise forms.ValidationError("please start a")
    return str(value)


