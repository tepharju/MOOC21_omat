# tee ratkaisu tänne

def eniten_kirjainta(mjono):
    r = 0
    s = 0
    for i in mjono:
        p = mjono.count(i)
        if p > r:
            r = p
            s = i
    return s



if __name__ == "__main__":
    eniten_kirjainta("abc")