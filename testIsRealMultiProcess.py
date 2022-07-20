import multiprocessing
import time
import cv2
from multiprocessing import Process
from multiprocessing import Queue

inPath = "D:\Application\\upupoo\\UpupooResource\\2000214068\sz.mp4"
outPath = "D:\Application\\upupoo\\UpupooResource\\2000214068\\out\\"

def add(i, queue):
    a = 0
    while True:
        if i == 1:
            queue.put(a)
            a += 1
        else:
            print("{}进程，取出{}".format(i, queue.get()))
        # time.sleep(1)

def readImg(st):
    vc = cv2.VideoCapture(inPath)
    vc.set(cv2.CAP_PROP_POS_FRAMES, st)
    for i in range(100):
        rval, frame = vc.read()
        cv2.imwrite(outPath+str(st)+str(i)+".jpg", frame)
    vc.release()


if __name__ == "__main__":
    # q = Queue(5)
    # for i in range(4):
    #     # Process(target=add, args=(i, q)).start()
    #     Process(target=readImg, args=(i*100,)).start()
    #     # 查看任务管理器 cpu核心占用判断是否是真多进程
    vc = cv2.VideoCapture(inPath)
    vc.set(cv2.CAP_PROP_POS_FRAMES, 120)
    for i in range(15):
        print(vc.get(i))
    rval, frame = vc.read()
    cv2.imwrite(outPath+"test1.jpg", frame)
    vc.release()