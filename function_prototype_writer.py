
# Designed for C
# Takes code from clipboard and pastes formatted function declarations back to clipboard.
# I.e. fn(void) {do stuff...} ==> fn(void);

import re, pyperclip


copied_array = str(pyperclip.paste())

# Remove brackets and anything inside them
rmBrackets = re.compile(r'{.*?\n}', re.DOTALL)

# Remove trailing comments
rmTrailing = re.compile(r'\)[ \t]*//[ \t]*[^\n]*\n')

# Add ';' at the end of functions that dont have them
addSemi = re.compile(r'\)[^;]')

# Remove excess \n after function if following function doesn't have comments
rmFnNl1 = re.compile(r'[\n\r]{3,}([^/]{2})')

# Remove excess \n of functions that have a comment (ignoring \n or \r) after them
rmFnNl2 = re.compile(r'[\n\r]{3,}')

# Remove excess forward slashes
rmExcSlash = re.compile(r'/{3,}')


# string = rmBrackets.findall(copied_array)
string = rmBrackets.sub(r'', copied_array)
string = rmTrailing.sub(r')', string)
string += '\n'  # Added so ';' can still be added if at end of string
string = addSemi.sub(r');\n', string)
string = rmFnNl1.sub(r'\n\1', string)
string = rmFnNl2.sub(r'\n\n', string)
string = rmExcSlash.sub(r'', string)

# Add comments around function prototypes
string =  "/////////////////// Function Prototypes ///////////////////\n" + string
string += "///////////////////////////////////////////////////////////"

pyperclip.copy(str(string))
print("Copied to Clipboard:\n", string)
