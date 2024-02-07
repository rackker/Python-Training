# Assignment: Annoying Text
original_text = " DYK that Python is named after Monty Python? "
# shouting_text = original_text.upper() is redundant, can be done in one variable
annoying_text = original_text.upper() * 10
print(annoying_text)
print(f"""My annonying text is {annoying_text}
It has {len(annoying_text)} characters""")


####### lesson notes ########

# Variables 
var = "Hello World"
print(var)

# Strings
var_upper = var.upper()
print(len(var_upper))
print(var + var + var)
print(var * 3)

multi_line_var = """testing
multi
line
strings"""
print(multi_line_var)

special_char_var = "use different quotes when using within string like this ' ' ' "
print(special_char_var)

format_string = "I can format strings"
print(f"guess what? {format_string}")