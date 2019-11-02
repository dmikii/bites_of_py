message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


s = message.split('\n')
print(s)
j = '|'.join(s)
print(j)



# def split_in_columns(message=message):
#     """Split the message by newline (\n) and join it together on '|'
#        (pipe), return the obtained output string"""
#     s = message.split('\n')
#     j = '|'.join(s)
#     return j
#
#
# split_in_columns(message)
# print(message)

