from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/<gurih>')
def hello_world(gurih):
    return gurih

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/crot', methods=['POST'])
def login():
	return request.form['anu']


@app.route('/input/alamat')
def alamat():
    alamat = [
    {
        'kodepos':40121,
        'kelurahan':'cicadas'
    },
    {
        'kodepos':40611,
        'kelurahan':'cigending'
    },
    {
        'kodepos':63463,
        'kelurahan':'plancungan'
    },
    {
        'kodepos' :20745,
        'kelurahan' :'damai'
    },
    {
        'kodepos' :34124,
        'kelurahan' :'tejosari'
    },
    {
        'kodepos' :40617,
        'kelurahan' :'Pasanggrahan'
    },
    {
        'kodepos' :20744,
        'kelurahan' :'kebun lada'
    },
    {
        'kodepos' :34112,
        'kelurahan' :'tejo agung'
    },
    {
        'kodepos' :63471,
        'kelurahan' :'mangunsuman'
    },
    {
        'kodepos' :34117,
        'kelurahan' :'banjar sari'
    },
    {
        'kodepos' :20743,
        'kelurahan' :'pahlawan'
    },
    {
        'kodepos' :40619,
        'kelurahan' :'Pasir Endah'
    }
]
    return jsonify({'daftar alamat':alamat})  #will return the json
