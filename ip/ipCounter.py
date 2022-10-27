def minmax(ip, mask):
    try:
        if 32 >= mask >= 0:
            mask = dec2ip(wild(2 ** (32 - mask) - 1))
    except:
        pass
    net = ip2dec(ip) & ip2dec(mask)
    wil = wild(ip2dec(mask))
    print(f"mask: {mask}\nwild:{dec2ip(wil)}")
    mi = net + 1
    ma = net + wil - 1
    hosts = wil - 1
    print(f"addresses: {dec2ip(mi)}->{dec2ip(ma)}\nhosts:{hosts}")


def ip2dec(ip):
    ipf = ""
    for i in ip.split(sep="."):
        buf = int(i)
        buf = bin(buf + 256)
        ipf += buf[3:]
    return int(ipf, 2)


# reverse bit
def wild(i):
    return abs(i - 2 ** 32 + 1)


def dec2ip(ip):
    out = ""
    for i in range(4):
        out += str(ip % 256) + "."
        ip >>= 8
    a = out.split(".")
    a.reverse()
    out = ""
    for i in a:
        out += i + "."
    return out[1:-1]


def show():
    ip = "196.168.100.102"
    mask = "255.255.255.0"
    minmax(ip, mask)
    minmax(ip, 30)

    ip = ip2dec(ip)
    mask = ip2dec(mask)
    wildcard = wild(mask)
    net = ip & mask
    # ip = bin(int(ip[0]), 8)[2:-1] + bin(int(ip[1]))[2:-1] + bin(int(ip[2]))[2:-1] + bin(int(ip[3]))[2:-1]
    # print(dec2ip(wildcard))
    # print(dec2ip(ip))
    # print(dec2ip(net))
    # print(dec2ip(mask))


if __name__ == "__main__":
    show()
