'''
The MIT License (MIT)
Copyright (c) 2013 Dave P.
'''

import asyncio
import signal
import sys
import ssl
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer, SimpleSSLWebSocketServer
from optparse import OptionParser
import json
from collections import defaultdict, deque

client_ping_times = defaultdict(list)
cliqueue = deque();

class SimpleEcho(WebSocket):

   def handleMessage(self):
       # kinds of messages...
       data = json.loads(self.data)
       print(data)
       # 1 - measure message to account for
        # { 'kind': 'ping', 'sent': 234234 , 'client' : 'nandaja'}
       if data['kind']  == 'ping':
           received_time = time.time()
           round_trip_time = received_time - data['sent_time']
           client_ping_times[data['client']].append(round_trip_time)

       # 2 - request from client to get current lag measurements


   def handleConnected(self):
       # add new client
       if self not in cliqueue:
           cliqueue.append(self)
       # begin (async?) loop that pings client every 5 secs?

   def handleClose(self):
       # remove client
       cliqueue.remove(self)


def begin_pinging(loop):
    # sends out pings every N seconds
    for client in cliqueue:
        data = {'sent_time': time.time(),
                'client': client.address,
                'kind': 'ping'}
        client.sendMessage(data)
        time.sleep(1)
    loop.call_later(5, begin_pinging, loop)

if __name__ == "__main__":

   parser = OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
   parser.add_option("--host", default='', type='string', action="store", dest="host", help="hostname (localhost)")
   parser.add_option("--port", default=8000, type='int', action="store", dest="port", help="port (8000)")
   parser.add_option("--example", default='echo', type='string', action="store", dest="example", help="echo, chat")
   parser.add_option("--ssl", default=0, type='int', action="store", dest="ssl", help="ssl (1: on, 0: off (default))")
   parser.add_option("--cert", default='./cert.pem', type='string', action="store", dest="cert", help="cert (./cert.pem)")
   parser.add_option("--ver", default=ssl.PROTOCOL_TLSv1, type=int, action="store", dest="ver", help="ssl version")

   (options, args) = parser.parse_args()

   cls = SimpleEcho

   server = SimpleWebSocketServer(options.host, options.port, cls)

   def close_sig_handler(signal, frame):
      server.close()
      sys.exit()

   signal.signal(signal.SIGINT, close_sig_handler)
   loop = asyncio.get_event_loop()
   loop.call_soon(begin_pinging, loop)
   loop.run_forever()
   server.serveforever()
