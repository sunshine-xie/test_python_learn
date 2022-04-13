import socket


# def main():
#     # 创建套接字
#     tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 链接服务器
#     server_ip = input("IP:")
#     server_port = int(input("Port:"))
#     server_addr = (server_ip, server_port)
#     tcp_socket.connect(server_addr)
#     while True:
#         # 发送数据
#         send_data = input("输入要发送的数据:")
#         if send_data == "exit()":
#             break
#         tcp_socket.send(send_data.encode("gbk"))
#         # 关闭套接字
#     tcp_socket.close()


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP和端口，''表示任何IP都可以
    tcp_server_socket.bind(("", 8087))
    # 从主动连接变为监听
    tcp_server_socket.listen(128)
    print("-------1---------")
    #
    while True:
        client_socket, client_addr = tcp_server_socket.accept()
        print("-------2---------")
        # 注意client_socket是创建了一个新的套接字，是一个类
        print("client_socket:", client_socket)
        # addr包含IP和Port
        print("client_addr:", client_addr)
        #
        # while True:
        #     recv_data = client_socket.recv(1024).decode("gbk")
        #     if recv_data == "exit()":
        #         break
        #     print(recv_data)
        #     #
        #     client_socket.send("hahah".encode("gbk"))
        #
        recv_data = client_socket.recv(1024).decode("gbk")
        print(recv_data)
        client_socket.send("hahah".encode("gbk"))
        client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()