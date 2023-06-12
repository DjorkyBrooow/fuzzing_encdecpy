from encdecpy import affine,atbash,autokey,baconian,base64,beaufort,caesar,columnartransposition,polybiussquare,railfence,rot13,runningkey,simplesubstitution,vignere
from random import randint
import random
import timeit

NB_ITER=1000

all_caps=[]
for i in range(65,91,1):
    all_caps+=chr(i)

all_low=[]
for i in range(97,123,1):
    all_low+=chr(i)

all_acc_char=[]
for i in range(192,382,1):
    all_acc_char+=chr(i)

all_char=all_caps+all_low+all_acc_char

ciphers = [
    'affine_cipher',
    'atbash_cipher',
    'autokey_cipher',
    'baconian_cipher',
    'base64_cipher',
    'beaufort_cipher',
    'caesar_cipher',
    'columnartransposition_cipher',
    'polybiussquare_cipher',
    'railfence_cipher',
    'rot13_cipher',
    'runningkey_cipher',
    'simplesubstitution_cipher',
    'vignere_cipher'
]

def create_word(min_length=1,max_length=10):
    word=""
    num=randint(min_length,max_length)

    for i in range(num):
        char=all_low[randint(0,len(all_low)-1)]
        word+=char
        
    return word

def create_sentence(min_word=1,max_word=10):
    sent=""
    num=randint(min_word,max_word)

    for i in range(num):
        word=create_word()
        sent+=word+' '

    return sent

def delete_rnd_char(sentence:str):
    num=randint(0,len(sentence)-1)
    sentence = sentence[:num]+sentence[num+1:]
    return sentence

def insert_rnd_char(sentence:str):
    num=randint(0,len(sentence)-1)
    char=all_low[randint(0,len(all_low)-1)]
    sentence=sentence[:num]+char+sentence[num:]
    return sentence

def flip_rnd_char(sentence:str):
    num=randint(0,len(sentence)-1)
    replace=all_char[randint(0,len(all_char)-1)]
    sentence=sentence[:num]+replace+sentence[num+1:]
    return sentence

def mutate(sentence:str):
    mutators = [
        delete_rnd_char,
        insert_rnd_char,
        flip_rnd_char
    ]
    mutator = random.choice(mutators)
    return mutator(sentence)

################################################################

# a and b are integers between 0 and 25. a should be relatively prime to 26 and lie between 0 to 25 (both inclusive).
def affine_cipher(sentence:str,a:int,b:int):
    sentence_e=affine.encode(sentence,a,b)
    sentence_d=affine.decode(sentence_e,a,b)
    return sentence_d
     
def affine_fuzzer(raw_sentence:str,dic_errors:dict,a:int,b:int):
    decoded_sentence=affine_cipher(raw_sentence,a,b)
    if raw_sentence!=decoded_sentence:
        dic_errors[raw_sentence]=affine_cipher.__name__
    return dic_errors

def affine_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    elem=[1,3,5,7,9,11,15,17,19,21,23,25]
    for i in range (nb):
        random.shuffle(elem)
        a=elem[0]
        b=randint(0,25)
        s=mutate(create_sentence())
        dic_errors=affine_fuzzer(s,dic_errors,a,b)
    return dic_errors

################################################################

def atbash_cipher(sentence:str):
    sentence_e=atbash.encode(sentence)
    sentence_d=atbash.decode(sentence_e)
    return sentence_d
     
def atbash_fuzzer(raw_sentence:str,dic_errors:dict):
    decoded_sentence=atbash_cipher(raw_sentence)
    if raw_sentence!=decoded_sentence:
        dic_errors[raw_sentence]=atbash_cipher.__name__
    return dic_errors

def atbash_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_sentence())
        dic_errors=atbash_fuzzer(s,dic_errors)
    return dic_errors

################################################################

# key is a string.
def autokey_cipher(sentence:str,key_str:str):
    sentence_e=autokey.encode(sentence,key_str)
    sentence_d=autokey.decode(sentence_e,key_str)
    return sentence_d
     
def autokey_fuzzer(raw_sentence:str,dic_errors:dict,key_str:str):
    decoded_sentence=autokey_cipher(raw_sentence,key_str)
    if raw_sentence.upper().replace(" ","")!=decoded_sentence:
        dic_errors[raw_sentence]=autokey_cipher.__name__
    return dic_errors

def autokey_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_sentence(min_word=5))
        key_str=mutate(create_word(min_length=5))
        dic_errors=autokey_fuzzer(s,dic_errors,key_str)
    return dic_errors


################################################################

def baconian_cipher(sentence:str):
    sentence_e=baconian.encode(sentence)
    sentence_d=baconian.decode(sentence_e)
    return sentence_d
     
def baconian_fuzzer(raw_sentence:str,dic_errors:dict):
    decoded_sentence=baconian_cipher(raw_sentence)
    if raw_sentence.upper()!=decoded_sentence:
        dic_errors[raw_sentence]=baconian_cipher.__name__
    return dic_errors

def baconian_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_sentence())
        dic_errors=baconian_fuzzer(s,dic_errors)
    return dic_errors

################################################################

def base64_cipher(sentence:str):
    sentence_e=base64.encode(sentence)
    sentence_d=base64.decode(sentence_e)
    return sentence_d
     
def base64_fuzzer(raw_sentence:str,dic_errors:dict):
    decoded_sentence=base64_cipher(raw_sentence)
    if raw_sentence!=decoded_sentence:
        dic_errors[raw_sentence]=base64_cipher.__name__
    return dic_errors

def base64_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_sentence())
        dic_errors=base64_fuzzer(s,dic_errors)
    return dic_errors

################################################################

# key is a string.
def beaufort_cipher(sentence:str,key_str:str):
    sentence_e=beaufort.encode(sentence,key_str)
    sentence_d=beaufort.decode(sentence_e,key_str)
    return sentence_d
     
def beaufort_fuzzer(raw_sentence:str,dic_errors:dict,key_str:str):
    decoded_sentence=beaufort_cipher(raw_sentence,key_str)
    if raw_sentence.upper().replace(" ","")!=decoded_sentence:
        dic_errors[raw_sentence]=beaufort_cipher.__name__
    return dic_errors

def beaufort_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_sentence(min_word=5))
        key_str=mutate(create_word(min_length=5))
        dic_errors=beaufort_fuzzer(s,dic_errors,key_str)
    return dic_errors


################################################################

# key is a whole number.
def caesar_cipher(sentence:str,key_int:int):
    sentence_e=caesar.encode(sentence,key_int)
    sentence_d=caesar.decode(sentence_e,key_int)
    return sentence_d
     
def caesar_fuzzer(raw_sentence:str,dic_errors:dict,key_int:int):
    decoded_sentence=caesar_cipher(raw_sentence,key_int)
    if raw_sentence!=decoded_sentence:
        dic_errors[raw_sentence]=caesar_cipher.__name__
    return dic_errors

def caesar_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_word())
        key_int=randint(1,25)
        dic_errors=caesar_fuzzer(s,dic_errors,key_int)
    return dic_errors

################################################################

# key is a string and should contain unique characters between A-Z.
def columnartransposition_cipher(sentence:str,key_str:str):
    sentence_e=columnartransposition.encode(sentence,key_str)
    sentence_d=columnartransposition.decode(sentence_e,key_str)
    return sentence_d
     
def columnartransposition_fuzzer(raw_sentence:str,dic_errors:dict):
    key_str=""
    tmp=all_caps.copy()
    random.shuffle(tmp)
    while(tmp!=[]):
        key_str+=tmp[0]
        tmp.remove(tmp[0])
    decoded_sentence=columnartransposition_cipher(raw_sentence,key_str)
    if raw_sentence!=decoded_sentence:
        dic_errors[raw_sentence]=columnartransposition_cipher.__name__
    return dic_errors

def columnartransposition_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_sentence())
        dic_errors=columnartransposition_fuzzer(s,dic_errors)
    return dic_errors

################################################################ 

# key is a string and should contain unique characters between a-z with one alphabet missing. 
# Length of key should be 25. An example key - phqgiumeaylnofdxkrcvstzwb.
def polybiussquare_cipher(sentence:str,key_str:str):
    try:
        sentence_e=polybiussquare.encode(sentence,key_str)
        sentence_d=polybiussquare.decode(sentence_e,key_str)
        return sentence_d
    except:
        return "error"
     
def polybiussquare_fuzzer(raw_sentence:str,dic_errors:dict):
    key_str=""
    tmp=all_low.copy()
    random.shuffle(tmp)
    tmp.remove(tmp[0])
    while(tmp!=[]):
        key_str+=tmp[0]
        tmp.remove(tmp[0])
    decoded_sentence=polybiussquare_cipher(raw_sentence,key_str)
    if raw_sentence!=decoded_sentence:
        dic_errors[raw_sentence]=polybiussquare_cipher.__name__
    return dic_errors

def polybiussquare_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_word())
        dic_errors=polybiussquare_fuzzer(s,dic_errors)
    return dic_errors

################################################################

# key is a positive number denoting the number of rails.
def railfence_cipher(sentence:str,key_int:int):
    sentence_e=railfence.encode(sentence,key_int)
    sentence_d=railfence.decode(sentence_e,key_int)
    return sentence_d
     
def railfence_fuzzer(raw_sentence:str,dic_errors:dict,key_int:int):
    decoded_sentence=railfence_cipher(raw_sentence,key_int)
    if raw_sentence!=decoded_sentence:
        dic_errors[raw_sentence]=railfence_cipher.__name__
    return dic_errors

def railfence_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_word())
        key_int=randint(2,10)
        dic_errors=railfence_fuzzer(s,dic_errors,key_int)
    return dic_errors

################################################################

def rot13_cipher(sentence:str):
    sentence_e=rot13.encode(sentence)
    sentence_d=rot13.decode(sentence_e)
    return sentence_d
     
def rot13_fuzzer(raw_sentence:str,dic_errors:dict):
    decoded_sentence=rot13_cipher(raw_sentence)
    if raw_sentence!=decoded_sentence:
        dic_errors[raw_sentence]=rot13_cipher.__name__
    return dic_errors

def rot13_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_word())
        dic_errors=rot13_fuzzer(s,dic_errors)
    return dic_errors

################################################################

# key is a large string, usually a paragraph taken from a book.
def runningkey_cipher(sentence:str,key_str:str):
    # try:
        sentence_e=runningkey.encode(sentence,key_str)
        sentence_d=runningkey.decode(sentence_e,key_str)
        return sentence_d
    # except:
    #     print(sentence+" : "+key_str)
    #     return "error"

def runningkey_fuzzer(raw_sentence:str,dic_errors:dict,key_str:str):
    decoded_sentence=runningkey_cipher(raw_sentence,key_str)
    if raw_sentence.upper().replace(" ","")!=decoded_sentence:
        dic_errors[raw_sentence]=runningkey_cipher.__name__
    return dic_errors

def runningkey_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_sentence(min_word=10, max_word=15))
        key_str=mutate(create_sentence(min_word=2,max_word=5))
        dic_errors=runningkey_fuzzer(s,dic_errors,key_str)
    return dic_errors

################################################################

# key is a string containing a permutation of the alphabets (a-z), 
# with no other characters. String should contain only unique characters.
def simplesubstitution_cipher(sentence:str,key_str:str):
    sentence_e=simplesubstitution.encode(sentence,key_str)
    sentence_d=simplesubstitution.decode(sentence_e,key_str)
    return sentence_d
     
def simplesubstitution_fuzzer(raw_sentence:str,dic_errors:dict):
    key_str=""
    tmp=all_low.copy()
    random.shuffle(tmp)
    while(tmp!=[]):
        key_str+=tmp[0]
        tmp.remove(tmp[0])
    decoded_sentence=simplesubstitution_cipher(raw_sentence,key_str)
    if raw_sentence!=decoded_sentence:
        dic_errors[raw_sentence]=simplesubstitution_cipher.__name__
    return dic_errors

def simplesubstitution_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_sentence())
        dic_errors=simplesubstitution_fuzzer(s,dic_errors)
    return dic_errors

################################################################

# key is a string, usually a single word.
def vignere_cipher(word:str,key_str:str):
    word_e=vignere.encode(word,key_str)
    word_d=vignere.decode(word_e,key_str)
    return word_d
     
def vignere_fuzzer(raw_word:str,dic_errors:dict,key_str:str):
    decoded_word=vignere_cipher(raw_word,key_str)
    if raw_word.upper()!=decoded_word:
        dic_errors[raw_word]=vignere_cipher.__name__
    return dic_errors

def vignere_repeat_fuzz(dic_errors:dict,nb:int=NB_ITER):
    for i in range (nb):
        s=mutate(create_word())
        key_str=mutate(create_word(min_length=2))
        dic_errors=vignere_fuzzer(s,dic_errors,key_str)
    return dic_errors

################################################################

def count_errors(dic_errors:dict):
    dic_count={
        'affine_cipher':0,
        'atbash_cipher':0,
        'autokey_cipher':0,
        'baconian_cipher':0,
        'base64_cipher':0,
        'beaufort_cipher':0,
        'caesar_cipher':0,
        'columnartransposition_cipher':0,
        'polybiussquare_cipher':0,
        'railfence_cipher':0,
        'rot13_cipher':0,
        'runningkey_cipher':0,
        'simplesubstitution_cipher':0,
        'vignere_cipher':0
    }
    for key,value in dic_errors.items():
        for elem in ciphers:
            if value==elem:
                dic_count[value]+=1
    return dic_count

def main():
    dic_errors={}
    dic_errors=vignere_repeat_fuzz(dic_errors)
    dic_errors=simplesubstitution_repeat_fuzz(dic_errors)
    dic_errors=runningkey_repeat_fuzz(dic_errors)
    dic_errors=rot13_repeat_fuzz(dic_errors)
    dic_errors=railfence_repeat_fuzz(dic_errors)
    dic_errors=polybiussquare_repeat_fuzz(dic_errors)
    dic_errors=columnartransposition_repeat_fuzz(dic_errors)
    dic_errors=caesar_repeat_fuzz(dic_errors)
    dic_errors=beaufort_repeat_fuzz(dic_errors)
    dic_errors=base64_repeat_fuzz(dic_errors)
    dic_errors=baconian_repeat_fuzz(dic_errors)
    dic_errors=autokey_repeat_fuzz(dic_errors)
    dic_errors=atbash_repeat_fuzz(dic_errors)
    dic_errors=affine_repeat_fuzz(dic_errors)

    for key,value in count_errors(dic_errors).items():
        print(key+" : "+str(value))
    

start = timeit.default_timer()
main()
stop = timeit.default_timer()
print('Time: ', stop - start) 
