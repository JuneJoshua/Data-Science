# Let's look at the lowercase letters.
import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "

# create `letters` here!
letters = dict(enumerate(alphabet))

encryption_key = 3

# define `encoding` here!
encoding = {letter: (place + encryption_key) % 27 for (place, letter) in enumerate(alphabet)}

message = "hi my name is caesar"

def caesar(message, encryption_key):
    encoding = {letter: (place + encryption_key) % 27 for (place, letter) in enumerate(alphabet)}
    coded_message = "".join([letters[encoding[letter]] for letter in message])
    return coded_message
    
encoded_message = caesar(message, encryption_key = 3)
print(encoded_message)


decoded_message = caesar(encoded_message, encryption_key = -3)
print(decoded_message)
