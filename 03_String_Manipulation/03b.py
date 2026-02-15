import difflib
def string_similarity(str1, str2):
    result = difflib.SequenceMatcher(a=str1.lower(), b=str2.lower)
    return result.ratio()

str1 = input ("Enter the string1")
str2 = input("Enter the string2")
print ("Original string:")
print(str1)
print(str2)
print("Similarity between two strings is ",string_similarity(str1,str2))