def encrypt(text,key):
	t=""
	caesar_key=int(key)%127

	for i in range(0,len(text)):
		ch=127-(ord(text[i])-1)+caesar_key
		
		if ch>127 :
			ch=ch-127

		t=t+chr(ch)

	return t

def decrypt(text,key):
	t=""
	caesar_key=int(key)%127

	for i in range(0,len(text)):
		ch=(ord(text[i])-caesar_key)
		if ch<1 :
			ch=128-1+ch

		ch=1+127-ch

		t=t+chr(ch)

	return t