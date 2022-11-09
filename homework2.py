#下图为PGP协议（RSA签名、RSA加密、IDEA消息加密的巧妙结合）的发送数据过程，
# 请编程模拟PGP协议收发数据过程，其中所涉及密码方案可做替换。
import hashlib
import secrets
import random
import base64
from RS import genenate_key,pow_mod
def PGP(k1,d1,k2,d2,M):#私钥，公钥
    #pgp的流程
    h= int(md5(M))
    #得到MAC
    EM=str(pow_mod(h,k1[2],d1[0]))#MAC经过A的私钥加密
    #对MAC进行加密
    EM=str(EM)+','+str(M)#拼凑明文和摘要。EM是摘要，M是明文
    # ZIP()
    EM,K=IDEA(EM)#维吉尼亚密码替换
    print(K)
    print("一次一密的密钥是，",int(K))
    EK = pow_mod(int(K),d2[1],d2[0])#使用B的公钥加密一次性密钥
    print("加密后的密钥是",EK)
    EM = str(EM)+','+str(EK)
    print("加密后的密文是",EM)
    EM = BASE64(EM,0)
    return EM,K
def md5(M):
    md=hashlib.md5()
    md.update(str(M).encode("utf8"))
    h = int(md.hexdigest(),16)
    return h
    M=A.dencypt(h,Kd,n)
    return M
def IDEA(EM):
    k=5
    em=''
    for i in range(len(EM)):
        E=ord(str(k))+ord(EM[i])
        em+=chr(E)
    return em,k
def IDEA_reverse(EM,K):
    em=''
    for i in range(len(EM)):
        E=ord(EM[i])-ord(str(K))
        em+=chr(E)
    return em

def BASE64(EM,flag):
    if flag==0:
        return base64.b64encode(EM.encode('utf-8')) 
    else:
        return str(base64.b64decode(EM),'utf-8')

def PGP_reverse(k1,d1,k2,d2,EM):#私钥，公钥
    EM=BASE64(EM,1)
    print("密文是",EM)
    #使用B的私钥解密出一次一密的密钥
    l = len(EM)
    place =EM.find(',')
    M=EM[0:place]
    EK=int(EM[place+1:l])
    print("加密后的一次一密密钥是",EK)
    Kl= pow_mod(EK,k2[2],d2[0])

    print("解密后的密钥是",Kl)
    #使用一次性密钥K对密文进行解密分离出密文和MAC
    M=IDEA_reverse(M,Kl)
    place= M.find(',')
    MAC=int(M[0:place])
    M=M[place+1:]
    M=888
    #使用A的公钥对MAC进行核实
    MAC=pow_mod(MAC,d1[1],d1[0])
    if MAC==md5(M):
        return True
    else:
        return False


if __name__ == "__main__":
    M=88888
    k1,d1=genenate_key()#k私钥，e公钥,加密时用到e1,e0,解密时用到k2,e0
    k2,d2=genenate_key()
    EM,K=PGP(k1,d1,k2,d2,M)#参数是A的私钥，B的公钥，明文,发送者，接收者
    print(EM)
    if(PGP_reverse(k1,d1,k2,d2,EM)):
        print("解密成功")
