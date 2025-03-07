



def longest(a, b):
    '''This function returns a string formed by combining two strings, a and b, 
    where duplicates are removed using the set function. Then, the characters are 
    sorted in ascending order (from a to z). Finally, the sorted characters are 
    joined together without any spaces between them.'''
    return ''.join(sorted(set(a + b)))

a = 'xyaabbbccccdefww'
b = 'xxxxyyyyabklmopq'

print()
print(longest(a,b))