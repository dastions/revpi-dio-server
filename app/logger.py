from datetime import datetime


def log(*args):
    time = datetime.now().strftime("[%d/%m/%Y - %H:%M:%S] - ")
    print(time,*args)
    # TODO: Store log