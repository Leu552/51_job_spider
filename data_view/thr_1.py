import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.2)
    print('T1 end\n')

def thread_job2():
    print('T2 start\n')
    print('T2 end\n')

def main():
    added_thread1 = threading.Thread(target=thread_job,name='T1')
    added_thread2 = threading.Thread(target=thread_job2,name='T2')
    added_thread1.start()
    added_thread2.start()
    print(threading.active_count())
    added_thread1.join()
    added_thread2.join()


    print('All done\n')


if __name__ == '__main__':
    print(len(str(499999999666666667166666666000000000)))