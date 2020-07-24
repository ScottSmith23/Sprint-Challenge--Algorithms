'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #initialize count value
    count = 0
    #return count when word length reaches less than 2
    if len(word) < 2:
        return count
    #increase count if first two letters are th
    if word[:2] == "th":
        count += 1
    #removes the first letter then puts it through the count_th function again
    word = word[1:]
    return count + count_th(word)
    
    
