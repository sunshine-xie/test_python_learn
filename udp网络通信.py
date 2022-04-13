import socket


def main():
    # 创建udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 从键盘接收数据
    while True:
        send_data = input("输入要发送的数据")
        if send_data == "exit()":
            break
        # 套接字收发数据
        # ip 和 端口号 写为元组
        # udp_socket.sendto(b"hahaha", ("127.0.0.1", 6000))
        udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1", 8080))

    # 关闭socket
    udp_socket.close()


if __name__ == "__main__":
    main()



