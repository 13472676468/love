# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/jinqu/<num>')
def jinqu(num):
    print(num,'i am {}'.format(num))
    vnc_url = 'http://www.guimp.com/'
    return render_template('./test.html', vnc_url=vnc_url)
    # return json.dumps({'state': 1})

#这个地方有点问题到底是谁的问题
#不是我的错
if __name__ == '__main__':
    app.run(port=5010)
