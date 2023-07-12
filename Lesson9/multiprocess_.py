import time
import multiprocessing

def f(i):
    time.sleep(2)
    print(i)

# start = time.time()
# p_list = []
# for i in range(10):
#     p = multiprocessing.Process(target=f, args=(i,))
#     p.start()
#     p_list.append(p)
#
# for i in p_list:
#     i.join()
start = time.time()
with multiprocessing.Pool() as pool:
    pool.map(f, list(range(10)))
print(time.time()-start)