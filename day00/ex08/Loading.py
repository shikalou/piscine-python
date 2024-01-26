import os
import time
import datetime as dt


def ft_tqdm(lst: range) -> None:
    """
    this script recreate the tqdm function which print a
    progress bar for a for loop using the yield keyword
    usage ->python3 tester.py
    """
    # print(ft_tqdm.__doc__)
    end = "\r"
    sta = dt.datetime.today().timestamp()
    for i in lst:
        dif = dt.datetime.today().timestamp() - sta
        fr = round(i/dif, 2)
        et = (lst.stop - i) / fr if fr > 0 else 0
        cu = time.time() - sta
        per = (i / lst.stop * 100)
        col = os.get_terminal_size().columns - 36
        pro = col * i / lst.stop
        s = "{}%|{:{len}}| ".format(int(per) + 1, "*" * int(pro), len=col)
        t = "{}/{} [{:.1f}<{:.1f}, {}it/s]".format(i + 1, lst.stop, cu, et, fr)
        print(s, t, end=end, sep="")
        yield i
