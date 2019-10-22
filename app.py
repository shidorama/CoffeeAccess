from flask import Flask

import config

app = Flask(__name__)
app.config.update(config.config_data)


@app.route('/ping')
def hello_world():
    return 'Hello World!'


@app.route('/auth_list')
def auth_list():
    return '-'


@app.route('/do_mm')
def do_mm():
    return '-'


@app.route('/do_em')
def do_em():
    return '-'


if __name__ == '__main__':
    app.run()
