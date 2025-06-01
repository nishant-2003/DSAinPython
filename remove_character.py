def remove_character(string,char):
    if len(string)== 0 or string==" ":
        return string
    mini_string=remove_character(string[1:],char)
    if string[0]==char:
        return mini_string
    else:
        return string[0]+mini_string


string="my name is Nizzzshantzzz Kumarzzz Jhzzza"
new_string=remove_character(string,"z")
print(new_string)
