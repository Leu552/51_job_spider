import multiprocessing as mp
import threading as td
import time

def job(q,a):
    res = 0
    print(mp.current_process())
    for i in range(a):
        res += i+i**2+i**3
    q.put(res)

def test():
    res = 0
    for _ in range(2):
        for i in range(1000000000):
            res += i+i**2+i**3
    return res

if __name__ == '__main__':
    q = mp.Queue()
    st = time.time()

    p1 = mp.Process(target=job,args=(q,1000000000/2))
    p2 = mp.Process(target=job,args=(q,1000000000/2))

    p1.start()
    p2.start()

    print(mp.cpu_count())
    p1.join()
    p2.join()
    st2 = time.time()
    print('多进程时间：',st2-st)
    res1 = q.get()
    res2 = q.get()

    print(res1+res2)
    test()
    print('normal时间：',time.time()-st2)