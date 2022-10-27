def minmax(ip, mask):
    ipf = ""
    maskf = ""
    for i in ip.split(sep="."):
        buf = int(i)
        buf = bin(buf + 256)
        ipf += buf[3:]
    # ipf.append(buf[3:])
    for i in mask.split(sep="."):
        buf = int(i)
        buf = bin(buf + 256)
        maskf += buf[3:]

    # ip = bin(int(ip[0]), 8)[2:-1] + bin(int(ip[1]))[2:-1] + bin(int(ip[2]))[2:-1] + bin(int(ip[3]))[2:-1]
    print(ipf)
    print(maskf)


def decToIp(ip):
    out = ""
    while ip > 0:
        out += ip % 256
        ip >>= 8;
    print(out)

if __name__ == "__main__":
    minmax("127.0.0.1", "255.255.255.0")
