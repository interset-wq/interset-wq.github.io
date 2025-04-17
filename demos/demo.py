from threading import Thread


def hi():
    for _ in range(10):
        print('hi')

for _ in range(5):
    thread = Thread(target=hi)
    thread.start()

