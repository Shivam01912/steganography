from PIL import Image
import mycipher as mcp

image=raw_input("Enter complete image file path : ")
img = Image.open(image)
rgb_img = img.convert('RGB')
pix=rgb_img.load()

width, height = img.size

key=raw_input("Enter the 4-digit PIN (Decryption Key) :")

bintext=""

p=""
count=0
for x in range(0,width):
	for y in range(0,height):
		r, g, b = rgb_img.getpixel((x, y))
		br=format(r,'08b')
		bg=format(g,'08b')
		bb=format(b,'08b')
		
		n=list(br)
		p=p+n[7]
		count=count+1

		if count==8:
			if p=="00000000":
				break
			else :
			 	bintext=bintext+chr(int(p,2))
			 	p=""
			 	count=0	

		n=list(bg)
		p=p+n[7]
		count=count+1


		if count==8:
			if p=="00000000":
				break
			else :
			 	bintext=bintext+chr(int(p,2))
			 	p=""
			 	count=0

		n=list(bb)
		p=p+n[7]
		count=count+1

		if count==8:
		 	if p=="00000000":
				break
			else :
			 	bintext=bintext+chr(int(p,2))
			 	p=""
			 	count=0

	if count==8:
		break


text=mcp.decrypt(bintext,key)

print "Message : ",text
print "Decryption Done...!!"	