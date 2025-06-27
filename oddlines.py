with open("song.txt",'w') as song:
    song.write("I, I just woke up from a dream\nWhere you and I had to say goodbye\nAnd I don't know what it all means\nBut since I survived, I realized\nWherever you go, that's where I'll follow\nNobody's promised tomorrow\nSo I'ma love you every night like it's the last night\nLike it's the last night\nIf the world was ending, I'd wanna be next to you\nIf the party was over and our time on Earth was through\nI'd wanna hold you just for a while and die with a smile\nIf the world was ending, I'd wanna be next to you")
with open('song.txt','r') as song:
    lyrics=song.readlines()
oddlines=lyrics[::2]
with open('lyrics.txt','w') as ly:
    ly.write("\n".join(oddlines))
with open('lyrics.txt','r') as ly:
    print(ly.read())
