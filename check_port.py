import socket
import os

def check_port(host,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        s.connect((host,port))
        s.shutdown(2)
    except OSError as msg:
        print('port %s is available!' %port)
        # print(msg)
        return True
    else:
        print('port %s already be in use! '%port)
        return False


def release_port(port):
    cmd_find='netstat -ano |findstr %s' %port
    print(cmd_find)

    result=os.popen(cmd_find).read()
    print(result)

    if str(port) and 'LISTENING' in result:
        i=result.index('LISTENING')
        start=i+len('LISTENING')+7
        end=result.index('\n')
        pid=result[start:end]

        cmd_kill='taskkill -f -pid %s' %pid
        print(cmd_kill)
        os.popen(cmd_kill)
    else:
        print('port %s is available' %port)



if __name__ == '__main__':
    host='127.0.0.1'
    port=4725
    # check_port(host,port)
    release_port(port)


