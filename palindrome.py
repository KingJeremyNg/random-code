def palindrome(string) :
    if len(string) <= 1 :
        return True
    elif string[0] == string[-1] :
        return palindrome(string[1:-1])
    else :
        return False