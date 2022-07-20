import time
import io
import sys
import tqdm
from tqdm import tqdm
from multiprocessing import Pool


def func(*a):
    for i in range(10):
        time.sleep(1)


if __name__ == "__main__":
    print(sys.getdefaultencoding())
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')            #改变标准输出默认编码为utf-8
    print(chr(0xf08d))
    
