import psutil
import time


def monitor():
    lastBytesRecv = psutil.net_io_counters().bytes_recv
    lastBytesSent = psutil.net_io_counters().bytes_sent

    while True:
        bytesRecv = psutil.net_io_counters().bytes_recv
        bytesSent = psutil.net_io_counters().bytes_sent

        recvData = bytesRecv - lastBytesRecv
        sentData = bytesSent - lastBytesSent

        print_to_console(recvData, sentData)

        lastBytesRecv = bytesRecv
        lastBytesSent = bytesSent

        time.sleep(1)


def print_to_console(recvData, sentData):
    dataRecv, typeRC = convert_to_corret(recvData)
    dataSent, typeST = convert_to_corret(sentData)

    if (typeRC == 0):
        print("Received " + "%0.1f" % dataRecv + " B/s")
    elif (typeRC == 1):
        print("Received " + "%0.1f" % dataRecv + " KB/s")
    elif (typeRC == 2):
        print("Received " + "%0.1f" % dataRecv + " MB/s")

    if (typeST == 0):
        print("Sent " + "%0.1f" % dataSent + " B/s")
    elif (typeST == 1):
        print("Sent " + "%0.1f" % dataSent + " KB/s")
    elif (typeST == 2):
        print("Sent " + "%0.1f" % dataSent + " MB/s")

    print('')


def convert_to_corret(bytes):
    if bytes/1024/1024 >= 1:
        return bytes/1024/1024, 2
    elif bytes/1024 >= 1:
        return bytes/1024, 1

    return bytes, 0


monitor()
