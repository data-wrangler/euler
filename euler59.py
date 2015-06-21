"""Euler 59: Brute-force cypher decryption

Each character on a computer is assigned a unique code and the preferred standard 
is ASCII (American Standard Code for Information Interchange). For example, 
uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. The advantage 
with the XOR function is that using the same encryption key on the cipher text, 
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

Your task has been made easy, as the encryption key consists of three lower case 
characters. Using cipher1.txt, a file containing the encrypted ASCII codes, and 
the knowledge that the plain text must contain common English words, decrypt the 
message and find the sum of the ASCII values in the original text.

my notes:
ok, so python ord(char) gives the ascii code, and chr(int) goes back to char.
xor cipher works thusly: convert both numbers to 8-bit binary and, one digit at 
a time, apply the XOR operator to generate that bit in the 
"""
from euler59_cipher1 import ciphertext

def xor(c,k):
	cbin=bin(c)[2:]
	kbin=bin(k)[2:]
	rbin=''
	if len(cbin)!=len(kbin):
		if len(cbin)>len(kbin):
			rbin=cbin[:(len(cbin)-len(kbin))]
			cbin=cbin[(len(cbin)-len(kbin)):]
		else:
			rbin=kbin[:(len(kbin)-len(cbin))]
			kbin=kbin[(len(kbin)-len(cbin)):]
	for i in range(len(cbin)):
		rbin+=str(int(cbin[i])^int(kbin[i]))
	rint=int(rbin,2)
	return rint

def to_plaintext(codelist):
	s=''
	for c in codelist:
		s+=chr(int(c))
	return s
	
def to_codelist(plaintext):
	c=[]
	for p in plaintext:
		c.append(ord(p))
	return c

def xcrypt(msg,key):
	ciph=[]
	for i in range(len(msg)):
		ciph.append(xor(msg[i],key[i%len(key)]))
	return ciph

def allkeys(keyposs,keylen):
	this_ak=keyposs
	for n in range(1,keylen):
		last_ak=this_ak
		this_ak=[]
		for m in keyposs:
			for o in last_ak:
				this_ak.append(o+m)
	return this_ak
	
def list_to_code(ptlist):
	codelist = []
	for pt in ptlist:
		codelist.append(to_codelist(pt))
	return codelist

def list_to_plain(codelist):
	ptlist=[]
	for cd in codelist:
		ptlist.append(to_plaintext(cd))
	return ptlist

def brute_force(ciph,keylist):
	allposs=[[],[]]
	for key in keylist:
		print "trying %s" % to_plaintext(key)
		allposs[0].append(to_plaintext(key))
		allposs[1].append(to_plaintext(xcrypt(ciph,key)))
	return allposs

alph = 'abcdefghijklmnopqrstuvwxyz'
alph_ak=allkeys(alph,3)
alph_code=list_to_code(alph_ak)

c1,c2,c3=[],[],[]
for i in range(0,len(ciphertext),3):
	c1.append(ciphertext[i])
	if i+1 < len(ciphertext):
		c2.append(ciphertext[i+1])
	if i+2 < len(ciphertext):
		c3.append(ciphertext[i+2])

ac=list_to_code(alph)

bf1=brute_force(c1,ac)
bf2=brute_force(c2,ac)
bf3=brute_force(c3,ac)

for i in range(len(bf1[0])):
	print "%s %s" % (bf1[0][i],bf1[1][i])


for i in range(len(bf2[0])):
	print "%s %s" % (bf2[0][i],bf2[1][i])


for i in range(len(bf3[0])):
	print "%s %s" % (bf3[0][i],bf3[1][i])

"""
key='god'
to_plaintext(xcrypt(ciphertext,to_codelist('god')))
"(The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He 
was with God, and he was God. 2 He was in the beginning with God. 3 He created 
everything there is. Nothing exists that he didn't make. 4 Life itself was in 
him, and this life gives light to everyone. 5 The light shines through the 
darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 
7 to tell everyone about the light so that everyone might believe because of his 
testimony. 8 John himself was not the light; he was only a witness to the light. 
9 The one who is the true light, who gives light to everyone, was going to come 
into the world. 10 But although the world was made through him, the world didn't 
recognize him when he came. 11 Even in his own land and among his own people, he 
was not accepted. 12 But to all who believed him and accepted him, he gave the 
right to become children of God. 13 They are reborn! This is not a physical birth 
resulting from human passion or plan, this rebirth comes from God.14 So the Word 
became human and lived here on earth among us. He was full of unfailing love and 
faithfulness. And we have seen his glory, the glory of the only Son of the Father."
"""
