"""
Modify the following word_distribution function so that
it returns a dictionary with the count of each word in
the input string.

Don't forget to put the words in lowercase.

If there's a punctuation sign at the end of a word, you should remove it.
You should remove only one punctuation sign if there are multiple signs.

Tests:

word_distribution("Hello. How are you? Please say hello if you don’t love me!")
should return {‘hello’: 2, ‘how’:1, ‘are’:1, ‘you’:2, ’please’:1, “don’t”: 1, 'say':1, 'if':1, 'love':1,'me':1}

word_distribution("That's when I saw Jane (John's sister)!")
should return {"that's":1, "when":1,"i":1,"saw":1,"jane":1, "john's":1, "sister)":1}
"""

def word_distribution(string):
    # change to lower case and convert into a list
    list = string.lower().split()

    # remove at most one instance of punctuation from beginning or end
    # as per assignment instructions
    for index in range(len(list)):
        if not list[index].isalpha():
            chars = [*list[index]]
            if not chars[0].isalpha():
                list[index] = ''.join(chars[1:len(chars)])
            elif not chars[len(chars)-1].isalpha():
                list[index] = ''.join(chars[0:len(chars)-1])

    # convert to a dictionary and count instances of repetition
    result = {index: 0 for index in list}

    # iterate through list and increment value if key exists in result
    for word in list:
        result[word] += 1

    return result
