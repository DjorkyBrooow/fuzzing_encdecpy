## Installation 

```$ pip install encdecpy```

## Usage 

Refer to [encdecpy](https://pypi.org/project/encdecpy/) for the documentation of the functions
The repository of the source is [here](https://github.com/IronVenom/encdecpy)

## Results of the fuzzer for each cipher and steps to find the errors :

### Affine

This cipher doesn't display any error in the console.
Errors with the caps : if there is a cap in the word you want to encode, it will be written as a lowercase in the encoded version.
The accented letters do not disturb the code process but they are not handled by the program. It means that they are not treated as letters and they don't change neither in the encoded or the decoded version.

Examples of wrong entries that don't provoke any error : 
- `affine.encode("hellô",5,23)` -> `'graaô'`
- `affine.encode("hellO",5,23)` -> `'graap'`

### Atbash

This cipher doesn't display any error in the console.
Same as affine about the accented letters 

Examples :
- `atbash.encode("hello")` -> `'svool'`
- `atbash.encode("hellô")` -> `'svooô'`

### Autokey

This cipher doesn't display any error in the console.
The accented letters are not considered as letters and disappear in the process of encoding.
The result given by both encode and decode function are in caps and without spaces, so I added this element to the verification of the fuzzer.

Examples : 
- `autokey.encode("hello","hi")` -> `'OMSPZ'`
- `autokey.encode("hellô","hi")` -> `'OMSP'`

### Baconian

No error in the console.
The result is given in caps with spaces so caps are handles the same way as lowercases.
The accented letters are not handled and like previously they disappear and this time they are replaced by spaces.

Examples :
- `baconian.encode("hello")` -> `'aabbbaabaaababbababbabbba'`
- `baconian.encode("hellô")` -> `'aabbbaabaaababbababb '`
- `baconian.encode("Hello you")` -> `'aabbbaabaaababbababbabbba bbaaaabbbababaa'`
- `baconian.encode("Hellô you")` -> `'aabbbaabaaababbababb  bbaaaabbbababaa'`

### Base64

I couldn't find any error in this cipher, it handles the accents and the caps accurately.

### Beaufort 

No error in the console.
The result is given in caps without spaces.
Accented letters are not considered as letters and are deleted from the string.

Examples : 
- `beaufort.encode("hello","hi")` -> `'AEWXT'`
- `beaufort.encode("Hello you","hi")` -> `'AEWXTKTO'`
- `beaufort.encode("Hellô you","hi")` -> `'AEWXJUN'`

### Caesar

No error in the console.
Accented letters are treated the same way as in affine, they are not treated by the program but they don't generate any error.

Examples :

- `caesar.encode("hello",5)` -> `'mjqqt'`
- `caesar.encode("hellô",5)` -> `'mjqqô'`
- `caesar.encode("Hellô",5)` -> `'Mjqqô'`

### Columnartransposition

Same as base64, I couldn't find any error in this cipher, it handles the accents and the caps accurately.

### Polybiussquare

An error occurs when the missing letter of the key (supposed to be composed of 25 unique letters of the alphabet) is in the word/sentence/string that you want to encode.
It doesn't make any difference between caps and lowercase (non accented letters only)
Accented letters are treated the same way as in caesar, they are not treated by the program but they don't generate any error.

Examples : 
The missing letter is the "w" :
- `polybiussquare.encode("How are you","azertyuiopmlkjhgfdsqnbvcx")` -> `KeyError: 'w'`
The missing letter is the "n" : 
- `polybiussquare.encode("How are you","azertyuiopmlkjhgfdsqwxcvb")` -> `'352451 111413 212422`
With an accented letter :
- `polybiussquare.encode("How are yôu","azertyuiopmlkjhgfdsqwxcvb")` -> `'352451 111413 21ô22'`


### Railfence

I didn't find any issue in this cipher.

### Rot13

No errors in the console.
Accented letters are not considered as letters and don't change in the encode and decode functions.

Examples : 
- `rot13.encode("hello")` -> `'uryyb'`
- `rot13.encode("hellô")` -> `'uryyô'`
- `rot13.encode("Hellô")` -> `'Uryyô'`

### Runningkey

I got an error in the console few times but I didn't manage to catch the reason of this error yet : `IndexError: string index out of range`.
The result is in caps and without spaces.
The accented letters in the string to encode are deleted and it's as if they don't exist.
The accented letters in the key are valued differently and count as a new letter.

Examples : 
- `runningkey.encode("hello how are you","hi everyone")` -> `'OMPGSYMKNVLGSP'`
- `runningkey.encode("hello how are yôu","hi everyone")` -> `'OMPGSYMKNVLGY'`
- `runningkey.encode("hello how are you","hi everyonë")` -> `'OMPGSYMKNYMCJY'`
- `runningkey.encode("hello how are yôu","hi everyonë")` -> `'OMPGSYMKNYMCP'`

### Simplesubstitution

No console errors.
Accented letters are not modified.

Examples :
- `simplesubstitution.encode("hello","pmolikujnyhbtgvrfcedxzswaq")` -> `'jibbv'`
- `simplesubstitution.encode("hellô","pmolikujnyhbtgvrfcedxzswaq")` -> `'jibbô'`

### Vignere

An error occured when the key word was composed of only accented letters : `IndexError: string index out of range`.
The result is in caps, without spaces.

Examples : 
Key composed of only accented letters :
- `vignere.encode("hello","ĥï")` -> `IndexError: string index out of range`
- `vignere.encode("hello","hi")` -> `'OMSTV'`
- `vignere.encode("hellô","hi")` -> `'OMST'`

## Time

To estimate the time of a loop, you can modify the global variable `NB_ITER` to increase the number of data to generate.

