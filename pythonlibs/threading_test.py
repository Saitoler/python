# -*- coding: utf-8 -*-

import time
import threading


def threading_test(*add):
    for argc in add:
        time.sleep(3)
        print(threading.current_thread().getName() + " " + argc)



if __name__ == "__main__":
    """
    threading 类发起新线程
    """
    
    print("main 主程序为 ", threading.current_thread())
    domains = ["http://c.biancheng.net/python/", "http://c.biancheng.net/shell/", "http://c.biancheng.net/java/"]
    thread = threading.Thread(target=threading_test, args=domains)
    thread.start()
    # thread.join()  # thread.join() 启用， 会阻塞调用该方法的线程，也就意味着，下面的 print 语句会在线程执行完再打印；
    # 不启用则是非阻塞式， 下面的 print 语句会先执行，线程会继续执行，直到运行结束
    print("main 程序 Done")


    """
    thread.join() 启用时程序的执行结果
    """
    # main 主程序为  <_MainThread(MainThread, started 4566623744)>
    # Thread-1 http://c.biancheng.net/python/
    # Thread-1 http://c.biancheng.net/shell/
    # Thread-1 http://c.biancheng.net/java/
    # main 程序 Done
    

    """
    thread.join() 不启用时程序的执行结果
    """
    # main 主程序为  <_MainThread(MainThread, started 4483483136)>
    # main 程序 Done
    # Thread-1 http://c.biancheng.net/python/
    # Thread-1 http://c.biancheng.net/shell/
    # Thread-1 http://c.biancheng.net/java/