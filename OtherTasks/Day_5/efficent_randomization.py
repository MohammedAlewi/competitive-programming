import random
def efficent_radomizer(max_num):
    random_num=[i+1 for i in range(max_num)]
    for i in range(max_num):
        num=random.randint(i,max_num-1)
        random_num[num],random_num[i]=random_num[i],random_num[num]
    return random_num

def main():
    print( efficent_radomizer(100))

if __name__=='__main__':main()