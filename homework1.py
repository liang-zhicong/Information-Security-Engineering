import hashlib
import random
import datetime
#实现密码学作业1

# – 参数： 哈希函数采用 SHA-256 ；挖矿难度为整数 d （ >0 ），代表哈希值前导字符串为 0 的数量， d 值越小难度越小， d 值越大难度越大
# – 1. 随机生成一个整数 x
# – 2. 对 x 生成哈希值 h=H(x)
# – 3. 对 h 的前导字符串进行判定：如为 d 个 0 则挖矿成功；否则回到步骤 1– 输出： d=1 ， 2 ， 3 ， 4 ， 5 时挖矿成功耗时（可取 3 组数平均值）

def main(d):
    x=random.randint(1,1e5)#生成大数
    #生成哈希值
    h=H(x)
    # h='0011'
    #判定步骤
    flag=determine(h,d)
    return flag
def H(x):
    x=str(x)
    md5=hashlib.sha256()  
    md5.update(x.encode("utf8"))
    h = md5.hexdigest()
    h=str(int(h,16))
    return h
def determine(h,d):
    z=h[0:d]
    # print(z)
    for i in z:
        if i!='8':
            return False
    return True
    


if __name__ == "__main__":
    for d in range(1,6,1):
        start = datetime.datetime.now()
        n=1
        while(n!=3):
            flag=main(d)#判定有多少个0才成功
            if flag==1:
                n=n+1
        end = datetime.datetime.now()
        print("前",d,"个数是8，花费的时间平均是毫秒：",(end-start).microseconds/1000/d)