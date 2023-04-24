# ipv4 functions

class CalcIpv4:
    def __init__(self, ip, mask):
        self.net = None
        self.hosts = None
        self.ma = None
        self.mi = None
        try:
            if 32 >= mask >= 0:
                mask = dec2ip(wild(2 ** (32 - mask) - 1))
        except:
            pass
        self.mask = mask
        self.minmax(ip, self.mask)

    def minmax(self, ip, mask):
        net = ip2dec(ip) & ip2dec(mask)
        wil = wild(ip2dec(mask))
        print(f"mask: {mask}\nwild:{dec2ip(wil)}")
        self.mi = net + 1
        self.ma = net + wil - 1
        self.hosts = wil - 1
        self.net = net
        # print(f"addresses: {dec2ip(mi)}->{dec2ip(ma)}\nhosts:{hosts}")

    def printing(self):
        print(f"net:{dec2ip(self.net)} with mask {self.mask} of hosts {self.hosts} "
              f"have ip range {dec2ip(self.mi)} ->\t{dec2ip(self.ma)}")

    # reverse bit


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


def ip2dec(ip):
    ipf = ""
    for i in ip.split(sep="."):
        buf = int(i)
        buf = bin(buf + 256)
        ipf += buf[3:]
    return int(ipf, 2)


def wild(i):
    return abs(i - 2 ** 32 + 1)


# def show():
#     ip = "196.168.100.102"
#     mask = "255.255.255.0"
#     minmax(ip, mask)
#     minmax(ip, 30)
#
#     ip = ip2dec(ip)
#     mask = ip2dec(mask)
#     wildcard = wild(mask)
#     net = ip & mask
#     # ip = bin(int(ip[0]), 8)[2:-1] + bin(int(ip[1]))[2:-1] + bin(int(ip[2]))[2:-1] + bin(int(ip[3]))[2:-1]
#     # print(dec2ip(wildcard))
#     # print(dec2ip(ip))
#     # print(dec2ip(net))
#     # print(dec2ip(mask))
def netOfSize(startIp, hosts):
    wil = hosts - 1
    mask = wild(dec2ip(wil))
    ip=CalcIpv4(startIp,mask)
    ip.printing()
def show():
    i1 = CalcIpv4("196.168.10.102", 30)
    i2 = CalcIpv4("127.10.1.100", 8)
    for i in range(i1.hosts):
        print(dec2ip(i1.mi + i))
    i1.printing()
    print(wild(ip2dec(i1.mask)))
    i2.printing()


if __name__ == "__main__":
    # show()
    netOfSize("193.140.0.15",4)
