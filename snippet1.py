# Code Snippet 1
db = open("output.txt", "w") # Changed to "w" mode to overwrite and create file
a = "Hello" + str(1) # You can sum a string with an integer, so I transformed 1 in a string
b = "How do you do?"
db.write(a + ", " + b + "\n")
db.close() # I wrote this line to close the db