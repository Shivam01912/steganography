from PIL import Image
import mycipher as mcp

image=raw_input("Enter complete image file path : ")
img = Image.open(image)
rgb_img = img.convert('RGB')
pix=rgb_img.load()

width, height = img.size

key=raw_input("Enter a 4-digit PIN (Encryption Key) :")
t=raw_input("Enter the Message : ")

text=mcp.encrypt(t,key)

bintext=""
for x in range(0,len(text)):
	bintext=bintext+str(format(ord(text[x]), '08b'))

bintext=bintext+"00000000"

count=0
for x in range(0,width):
	for y in range(0,height):
		r, g, b = rgb_img.getpixel((x, y))
		br=format(r,'08b')
		bg=format(g,'08b')
		bb=format(b,'08b')
		
		n=list(br)
		n[7]=bintext[count]
		br="".join(n)
		count=count+1

		if count==len(bintext):
			pix[x,y]=(int(br,2),int(bg,2),int(bb,2))

			break			

		n=list(bg)
		n[7]=bintext[count]
		bg="".join(n)
		count=count+1


		if count==len(bintext):
			pix[x,y]=(int(br,2),int(bg,2),int(bb,2))

			break

		n=list(bb)
		n[7]=bintext[count]
		bb="".join(n)
		count=count+1

		if count==len(bintext):
			pix[x,y]=(int(br,2),int(bg,2),int(bb,2))

			break
		
		pix[x,y]=(int(br,2),int(bg,2),int(bb,2))
	
	if count==len(bintext):
		break

rgb_img.save("encrypted.png")

print "Encryption Done...!!"
print "Share the key with the person you share the image with, to decrypt"