
def abc_1000_demo1():  #这个算法不好
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a+b+c==1000 and a**2 + b**2 == c**2:
                    print("a,b,c:%d,%d,%d"%(a,b,c))

def abc_1000_demo2():  #这个算法不好
    for a in range(1001):
        for b in range(1001):
            c = 1000 -a -b
            if  a**2 + b**2 == c**2:
                print("a,b,c:%d,%d,%d"%(a,b,c))

if __name__ == '__main__':
    # abc_1000_demo1()
    abc_1000_demo2()