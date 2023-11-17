glossary = {
  'function': """a function is a group of related statements that performs a specific task
  """, 
  'string': """ string are arrays of bytes representing unicode characters
  """,
  'break': """in Python 'break' is a loop control statement
  """, 
  'dictionary': """dictionaries are Python’s implementation of a data structure that is more generally known as an associative array
   """, 
  'list': """lists are used to store multiple items in a single variable
  """,
    }

word = 'function'
print(word.title() + " : " + glossary[word])

word = 'string'
print(word.title() + " : " + glossary[word])

word = 'break'
print(word.title() + " : " + glossary[word])

word = 'dictionary'
print(word.title() + " : " + glossary[word])

word = 'list'
print(word.title() + " : " + glossary[word])