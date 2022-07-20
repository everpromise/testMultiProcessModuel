import multiprocessing
import time
import tqdm
from tqdm import tqdm, trange
from multiprocessing import Pool, Process


def func(k, midtime, limit, lock):
    # print("\n\n\n\n\n\n", end="")
    for i in range(limit):
        lock.acquire()
        print("\x1b["+ str(k)+"A\r {}进程 : ".format(k) + i*'*', "\x1b["+ str(k)+"B\r", end="")
        lock.release()
        time.sleep(midtime)


if __name__ == "__main__":
    print("\n\n\n\n\n\n", end="")
    lock = multiprocessing.Lock()
    midtime = [0.5, 0.1, 0.2, 1.0]
    limit = [100, 150, 50, 100]
    p_list = []
    start = time.time()
    for cnt in range(1, 5):
        p = Process(target=func, args=(cnt,midtime[cnt-1],limit[cnt-1],lock,))
        p.start()
        p_list.append(p)
    for j in p_list:
        j.join()
    end = time.time()
    print("\n应用多进程耗时: %0.2f seconds" % (end - start))


    # #甚至不需要import
    # while True:
    #     print('Pls input a number:', end='')
    #     num = input()
    #     if num.isdigit(): #判断输入是否是纯数字(不包括'-')
    #         num=int(num)
    #         break
    #     else:
    #         print('\x1b[1A\x1b[2K'+'\r*****  '+'\x1b[1;31m'+'Not A Number!'+'\x1b[0m'
    #                 +'  *****', end='')
    #     time.sleep(3) #这个记得import time
    #     print('\x1b[2K\r')
    # print("1\n2\n3\n4\n5\n", end="")

    # print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # print("\x1b[1A\r" + "这是最后一行", end="")
    # print("\x1b[1A\r" + "这是倒数第1行", end="")
    # print("\x1b[1A\r" + "这是倒数第2行", end="")
    # print("\x1b[1A\r" + "这是倒数第3行", end="")
    # print("\x1b[1A\r" + "这是倒数第4行", end="")
    # print("\x1b[1A\r" + "这是倒数第5行", end="")
    # print("\x1b[1A\r" + "这是倒数第6行", end="")
    # print("\x1b[1A\r" + "这是倒数第7行", end="")
    # print("\x1b[1A\r" + "这是倒数第8行", end="")
    # print("\x1b[7B\r")
    # print("\x1b[1A\r" + "               这是倒saf数第8行", end="")

    # print("\n\n\n\n\n")
    # # print("\x1b[1A\r" + "这是最后一行", end="")
    # # print("\x1b[1A\r" + "这是倒数第1行", end="")
    # print("\x1b[5A\r" + "这是倒数第3行", end="")
    # print("\x1b[3B\r")
    # print("\x1b[3A\r" + "这是倒数第2行", end="")
    # print("\x1b[1B\r")    
    # print("\x1b[1A\r" + "这是倒数第1行", end="")
    # print("\x1b[1B\r" + "fjdalksaaaaaaaaaaaaaaaaaaa", end="")
    # print("\x1b[4A\r" + "sssssssssssss这是倒数第3行", end="")
    # print("\x1b[3B\r")

    # print("\n\n\n\n\n")  # 这段代码是成功的
    # for i in range(12):
    #     if i % 2 == 0:
    #         print("\x1b["+str(1)+"A\r" , i, "\x1b[1B\r",  end="")
    #         # print("\x1b[1B\r", end="")
    #     else:
    #         print("\x1b[2A\r" , i, end="")
    #         print("\x1b[2B\r", end="")
    #     time.sleep(0.5)
    #     print("\x1b[3A\r" , i, end="")
    #     print("\x1b[3B\r", end="")        
    #     print("\x1b[0A\r" , "success"+str(i), end="")
    #     print("\x1b[0B\r", end="")


    # print("\x1b[2E")    
    # print("\x1b[3A" + "这是倒数第3行")
    # print("\x1b[3B")
    # print("\x1b[2A" + "这是倒数第2行" + "\x1b[2B")
    # print("\x1b[3A" + "这是倒数第3行" + "\x1b[3B")
    # print("\x1b[4A" + "这是倒数第4行" + "\x1b[4B")
    # print("\x1b[u\x1b[2A" + "world")
    # print("\x1b[3B")
    # print("\x1b[u\x1b[1A" + "woldddddddddddddddddddd")
    # print("\x1b[u\x1b[s" + "song")
    # print("\x1b[u\x1b[3A" + "song")
    # print('\x1b[1A\r' + "4", end="")
    # for i in range(13):

    # print('\x1b[3A' + "j", end="")
    # print('\x1b[10A\x1b[2B' + "k", end="")
    # print('\x1b[1A\r' + "2", end="")
    # print('\x1b[1A\r' + "1", end="")
    # pool = Pool()
    # for a in pool.imap_unordered(func=func):

    # for i in range(3):
    #     pool.apply(func)

    
