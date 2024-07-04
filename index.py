def solution(N):
    import string
    letters = string.ascii_lowercase 
    num_letters = len(letters)
    result = []

# Determining the number of full sets of letters we can use
    full_sets = N // num_letters  
    remainder = N % num_letters  

# Adding full sets of letters
    for _ in range(full_sets):
        result.extend(letters)

# Adding the remaining letters
    result.extend(letters[:remainder])

    return ''.join(result)  