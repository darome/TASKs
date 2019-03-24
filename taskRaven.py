#Write a function that takes as input two strings: 
# 1.	the message you want to write
# 2.	all the letters found in your bowl of alphabet soup.
#Assumptions: 
# •	It may be a very large bowl of soup containing many letters.
# •	There is no guarantee that each letter occurs a similar number of times - indeed some letters might be missing entirely.
# •	The letters are ordered randomly.
# The function should determine if you can write your message with the letters found in your bowl of soup. The function should return True or False accordingly. 
# Try to make your function efficient. Please use Big-O notation to explain how long it takes your function to run in terms of the length of your message (m) and the number of letters in your bowl of soup (s). 



def function_soup(message, soup):

    #array to save the soup letters
    letras = set ()

    # we set it to true because in case we dont find the letter in the message we return false, otherwise will be true
    x = True

    #retrieve the letters from the soup = O(s)
    for letter in soup:
        letras.add(letter)


    #COMPARAMOS CADA LETRA CON LAS LETRAS DEL MENSAJE = O(m)
    for letter in message:
        # SI LA LETRA NO ESTA EN NUESTRO MENSAJE KO = O(l)
        if letter not in letras:
            x = False
            break

    return x

    # O(s)> = O(l)
    # O(l) is a subset of O(s) to avoid a repetition
    # WORST CASE O(l) * O(m) = O(l*m)
    # BEST CASE O(1)*O(1) = O(1)
