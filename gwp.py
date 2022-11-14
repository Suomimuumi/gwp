P='ssid'
O='Profile'
F=':'
C=str
B=print
import subprocess as D,os,re
from collections import namedtuple as E
import configparser as K
def J():
	B=D.check_output('netsh wlan show profiles').decode();A=[];C=re.findall('All User Profile\\s(.*)',B)
	for E in C:G=E.strip().strip(F).strip();A.append(G)
	return A
def A(verbose=1):
	K=J();M=E(O,[P,'ciphers','key']);C=[]
	for G in K:
		H=D.check_output(f'netsh wlan show profile "{G}" key=clear').decode();B=re.findall('Cipher\\s(.*)',H);B='/'.join([A.strip().strip(F).strip()for A in B]);A=re.findall('Key Content\\s(.*)',H)
		try:A=A[0].strip().strip(F).strip()
		except IndexError:A='None'
		I=M(ssid=G,ciphers=B,key=A)
		if verbose>=1:L(I)
		C.append(I)
	return C
def L(profile):A=profile;B(f"{A.ssid:25}{A.ciphers:15}{A.key:50}")
def G(verbose):B('SSID                     CIPHER(S)      KEY');A(verbose)
def H(verbose=1):
	J='_';I='-';B='/etc/NetworkManager/system-connections/';A=[P,'auth-alg','key-mgmt','psk'];L=E(O,[B.replace(I,J)for B in A]);C=[]
	for N in os.listdir(B):
		D={B.replace(I,J):None for B in A};F=K.ConfigParser();F.read(os.path.join(B,N))
		for (S,Q) in F.items():
			for (G,R) in Q.items():
				if G in A:D[G.replace(I,J)]=R
		H=L(**D)
		if verbose>=1:M(H)
		C.append(H)
	return C
def M(profile):A=profile;B(f"{C(A.ssid):25}{C(A.auth_alg):5}{C(A.key_mgmt):10}{C(A.psk):50}")
def I(verbose):B('SSID                     AUTH KEY-MGMT  PSK');H(verbose)
def N(verbose=1):
	A=verbose
	if os.name=='nt':G(A)
	elif os.name=='posix':I(A)
	else:raise NotImplemented('Code only works for either Linux or Windows')
if __name__=='__main__':N()