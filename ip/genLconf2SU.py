# generate startup files from lab.conf
import re


def split(name):
    try:
        out = re.split('(\[|\]=|\n)', name)
        out = [out[0], out[2], out[4]]
    except:
        out = -1
    finally:
        return out;


def readLab(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    router = dict()
    domen = dict()

    for line in lines:
        if line[0] != "#":
            l = split(line);
            if l != -1:
                router[l[0]] = [l[1], l[2]]
                domen[l[2]] = [l[1], l[0]]

    print(domen)


if __name__ == "__main__":
    readLab('lab.conf')
