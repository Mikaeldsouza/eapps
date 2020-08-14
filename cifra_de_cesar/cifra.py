def generate_alt_alphabet(local_alphabet,local_key):
    local_alt_alphabet = []
    for i in range(local_key):
        local_alt_alphabet.insert(0,local_alphabet.pop())
    for i in local_alphabet:
        local_alt_alphabet.append(i)
    return local_alt_alphabet


def replace_alphabet_to_alt_alphabet(local_text,local_alphabet,local_alt_alphabet):
    local_replaced_text = []
    for i in local_text:
        try:
            local_replaced_text.append(local_alt_alphabet[local_alphabet.index(i)])
        except ValueError:
            local_replaced_text.append(i)
    return "".join(local_replaced_text)



def crypt(text,key):
    text = text.lower()
    alphabet = [chr(i) for i in range( ord("a"), ord("z")+1 )]
    alt_alphabet = generate_alt_alphabet(list(alphabet),key)
    if ( 0 < key <=25 ) :
        return replace_alphabet_to_alt_alphabet(text,list(alphabet),alt_alphabet)
    raise ValueError("Key must be less than 26 and more than 0.")
