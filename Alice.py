#! /usr/bin/python
# -*-coding:Latin-1 -*
import socket;
import random;
from Crypto.Cipher import AES


if __name__ =="__main__":
	hote = "localhost";
	port = 15555;
	
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	socket.connect((hote, port));
	
	print("Envoi des paramètres à Bob afin de procéder à l'échange de clés de Diffie-Hellman");
	print("Nous choisissons le groupe de Diffie-Hellman n°14 avec les paramètres suivants : \n");
	
	a = random.randint(1,100);
	p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
	g = 2;
	A = g^a%p;
	
	
	print("p = FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1 29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245 E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F 83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D 670C354E 4ABC9804 F1746C08 CA18217C 32905E46 2E36CE3B E39E772C 180E8603 9B2783A2 EC07A28F B5C55DF0 6F4C52C9 DE2BCBF6 95581718 3995497C EA956AE5 15D22618 98FA0510 15728E5A 8AACAA68 FFFFFFFF FFFFFFFF \ng = 2 \nA = " + str(A));
	socket.send("A = " + str(A));
	data = socket.recv(1024);
	print data;
	B = data.split("= ")[1];
	print B
	secretCommun = long(B)^a%p;
	print secretCommun;
	data = socket.recv(1024);
	C = data.split("= ")[1];
	vecteurInitialisationCommun = "C'est l'IVcommun";
	dechiffrement = AES.new(str(secretCommun).zfill(16), AES.MODE_CBC, vecteurInitialisationCommun);
	texteDechiffre = dechiffrement.decrypt(C);
	texteDechiffre = texteDechiffre.replace('0', '');
	print texteDechiffre
	
	socket.close();
