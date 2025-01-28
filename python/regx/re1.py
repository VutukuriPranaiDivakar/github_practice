# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.


"""

Metacharacters ::
[]  ::	A set of characters	"[a-m]"	
\	::  Signals a special sequence (can also be used to escape special characters)	"\d"	
.   ::	Any character (except newline character)	"he..o"	
^   ::	Starts with	"^hello"	
$   ::	Ends with	"planet$"	
*   ::	Zero or more occurrences	"he.*o"	
+   ::	One or more occurrences	"he.+o"	
?   ::	Zero or one occurrences	"he.?o"	
{}  ::	Exactly the specified number of occurrences	"he.{2}o"	
|   ::	Either or	"falls|stays"	
()  ::	Capture and group


Special Sequences ::
\A  :: Returns a match if the specified characters are at the beginning of the string ::"\AThe"	
\b  :: Returns a match where the specified characters are at the beginning or at the end of a word :: r"\bain"
\B  :: Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word :: r"\Bain"
\d  ::  Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D  ::  Returns a match where the string DOES NOT contain digits	"\D"
\s  ::  Returns a match where the string contains a white space character	"\s"	
\S  ::  Returns a match where the string DOES NOT contain a white space character	"\S"	
\w  ::  Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W  :: Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z  :: Returns a match if the specified characters are at the end of the string	"Spain\Z"

"""
import re
# search ::
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned 

sentence = "Python is a interpreter language and high level language."
pattern = "High"
a = re.search(pattern, sentence)

if a:
    print("Correct")
else:
    print("Incorrect")

# Match ::
# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


