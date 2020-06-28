from threading import Thread


def spider():
    '''线程事件函数'''
    print('I am spider man')

t_list = []

for i in range(5):
    t = Thread(target=spider)
    t_list.append(t)
    t.start(s)

for t in t_list:
    t.join()