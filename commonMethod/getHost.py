# -*- coding:utf-8 -*-
import socket


class GetHost():
    """
    获取本机ipv4地址
    """

    @classmethod
    def host(cls):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.connect(('10.0.0.1',8080))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip


if __name__ == '__main__':
    print(GetHost.host())