song="oman,buy some green onion and white onion from the onion market, while you are at it buy some spring onion as well"
f_char=song[0]
song=f_char+song[1:].replace('o','$')
print(song)
