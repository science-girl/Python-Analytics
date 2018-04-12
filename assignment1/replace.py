"""
Modify the following replace function so that where the first occurrence of
replace_string in test_string is replaced by bodega.

Tests:

replace("Hi how are you?", "you") should return "Hi how are bodega?"

replace("Love is in the air", "air") should return "Love is in the bodega"
"""

def replace(test_string, replace_string):
   if(test_string.find(replace_string) > 0):
    return test_string.replace(replace_string, "bodega");
   else:
    return test_string;