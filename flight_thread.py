from threading import *
import time
class Flight:
    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = Lock()

    def reserve(self, need_seat):
        self.l.acquire(blocking= True, timeout=2 )
        print('available seat: ',self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat alloted for {name}')
            self.available_seat -= need_seat
            time.sleep(4)

        else:
            print('sorry all seat has alloted')
        self.l.release()

if __name__ == '__main__':
    f = Flight(2)
    t1 = Thread(target=f.reserve, args=(1,), name = 'santosh')
    t2 = Thread(target=f.reserve, args=(1,), name = 'manoj')
    t3 = Thread(target=f.reserve, args=(1,), name = 'kiran')
    t1.start()
    t2.start()
    t3.start()