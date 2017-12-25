import random

def encrypt(text,key):
	t=""
	random.seed(int(key))
	caesar_key=random.randint(1,127)

	for i in range(0,len(text)):
		ch=127-(ord(text[i])-1)+caesar_key
		
		if ch>127 :
			ch=ch-127

		t=t+chr(ch)

	return t

def decrypt(text,key):
	t=""
	random.seed(int(key))
	caesar_key=random.randint(1,127)

	for i in range(0,len(text)):
		ch=(ord(text[i])-caesar_key)
		if ch<1 :
			ch=128-1+ch

		ch=1+127-ch

		t=t+chr(ch)

	return t