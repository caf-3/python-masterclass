from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count())
    five_hundred_millions = 125000000
    a = Process(target=counter, args=(five_hundred_millions, ))
    b = Process(target=counter, args=(five_hundred_millions, ))
    c = Process(target=counter, args=(five_hundred_millions, ))
    d = Process(target=counter, args=(five_hundred_millions, ))
    e = Process(target=counter, args=(five_hundred_millions, ))
    f = Process(target=counter, args=(five_hundred_millions, ))
    g = Process(target=counter, args=(five_hundred_millions, ))
    h = Process(target=counter, args=(five_hundred_millions, ))
    
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    

    print(f'Finished in {time.perf_counter()} seconds')

if __name__ == '__main__':
    main()