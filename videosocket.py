import socket

class videosocket:
    '''A special type of socket to handle the sending and receiveing of fixed
       size frame strings over ususal sockets
       Size of a packet or whatever is assumed to be less than 100MB
    '''

    def __init__(self , sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            print "not none"
            self.sock= sock

    def connect(self,host,port):
        self.sock.connect((host,port))

    def vsend(self, framestring):
        print "vsend"
        totalsent = 0
        metasent = 0
        length =len(framestring)
        lengthstr=str(length).zfill(8)

        while metasent < 8 :
            sent = self.sock.send(lengthstr[metasent:])
            if sent == 0:
                raise RuntimeError("Socket connection broken")
            metasent += sent
        
        
        while totalsent < length :
            sent = self.sock.send(framestring[totalsent:])
            if sent == 0:
                raise RuntimeError("Socket connection broken")
            totalsent += sent

    def vreceive(self):
        totrec=0
        metarec=0
        msgArray = []
        metaArray = []
        while metarec < 8:
            chunk = self.sock.recv(8 - metarec)
            if chunk == '':
                break
                # raise RuntimeError("Socket connection broken")
            print "h"
            metaArray.append(chunk)
            metarec += len(chunk)
        lengthstr= ''.join(metaArray)
        length=int(lengthstr)

        while totrec<length :
            chunk = self.sock.recv(length - totrec)
            if chunk == '':
                break
                # raise RuntimeError("Socket connection broken")
            msgArray.append(chunk)
            totrec += len(chunk)
        print "received"
        return ''.join(msgArray)

   


        
