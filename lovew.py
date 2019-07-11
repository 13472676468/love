# -*- coding: utf-8 -*-
from flask import Flask, render_template
import json
app = Flask(__name__)


@app.route('/jinqu/<num>')
def jinqu(num):
    print(num,'i am {}'.format(num))
    # vnc_url = 'http://www.yuu1.com/flsd/tags/dyp.html'
    return render_template('./testw.html')
    # return json.dumps({'state': 1})
#好好好打搜啊房间里卡都是放假了卡仕达解放路上打开积分卡死啦安居房
if __name__ == '__main__':
    app.run(port=5010,debug=True)