""" The module contains string formatting exercises """

err_numb = 50159747054
name = "Alex"
doc_link = "https://docs.python.org/3/library/stdtypes.html#:~:text=string%20objects%20have%20one%20unique%20built-in%20operation%3A%20the%20%25%20operator%20(modulo)"

# OLD STYLE STRING FORMATTING
greeting = "Hello, %s" % name
print(greeting)

# there are a lot of format specifier, just check doc_link
some_error = "Ups .. %x occurred" % err_numb
print(some_error)

# multiply substitution
massage_tuple = "Hey, %s, there is  some error: %x" % (name, err_numb)
print(massage_tuple)
massage_dict = "Hey, %(name)s, there is  some error: %(err_numb)x" % {"name": name, "err_numb": err_numb}
print(massage_dict)

# NAW STYLE STRING FORMATTING
some_string = "Hello! my name is {}. Have you ever have this type of error: {}".format(name, err_numb)
print(some_string)
some_string_ = "Hello! my name is {name}. Have you ever have this type of error: {err_numb:x}".format(name=name,
                                                                                                      err_numb=err_numb)
print(some_string_)

# F-STRINGS
print(f"This method looks much easier, you just put some values into square brackets: {name}, {err_numb:#x}")

# TASK
format_string = "Hello {} {}. Your current balance is ${:f}".format("John", "Doe", 53.44)
print(format_string)
