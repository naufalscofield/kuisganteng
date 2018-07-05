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
@app.route('/input/mahasiswa')
def mahasiswa():
    mahasiswa = [
    {
        'npm':1164001,
        'nama':'aldi'
    },
    {
        'npm':1164019,
        'nama':'naufal'
    },
    {
        'npm':1164026,
        'nama':'rojasqi'
    },
    {
        'npm':1164025,
        'nama':'rizal'
    },
    {
        'npm':1164012,
        'nama':'farhan'
    },
    {
        'npm':1164009,
        'nama':'ikri'
    },
    {
        'npm':1164011,
        'nama':'esi'
    },
    {
        'npm':1164013,
        'nama':'ema'
    },
    {
        'npm':1164020,
        'nama':'ojack'
    },
    {
        'npm':1164021,
        'nama':'seta'
    }
]
    return jsonify({'daftar mahasiswa':mahasiswa})  #will return the json

@app.route('/negara/kota')
def kota():
    kota = [
    {
        'kota':'Bandung'
    },
    {
        'kota':'Jakarta'
    },
    {
        'kota':'Surabaya'
    },
    {
        'kota':'Palembang'
    },
    {
        'kota':'Medan'
    },
    {
        'kota':'Lampung'
    },
    {
        'kota':'Makasar'
    },
    {
        'kota':'Aceh'
    },
    {
        'kota':'Semarang'
    },
    {
        'kota':'Padang'
    },
    {
        'kota':'Purwokerto'
    }
]
    return jsonify({'daftar kota':kota})  #will return the json

@app.route('/kampus/bandung', methods=['GET'])
def kampus():
    kampus = [
    {
        'universitas':'Unpar'
    },
    {
        'universitas':'Maranatha'
    },
    {
        'institut':'ITB'
    },
    {
        'politeknik':'Polban'
    },
    {
        'universitas':'UPI'
    },
    {
        'universitas':'Unpad'
    },
    {
        'politeknik':'poltekpos'
    },
    {
        'universitas':'Unisba'
    },
    {
        'politeknik':'Polman'
    },
    {
        'institut':'ITENAS'
    }
]
    return jsonify({'daftar kampus di Bandung':kampus})  #will return the json

@app.route('/brand/tas', methods=['GET'])
def merektas():
    merektas = [
    {
        'tas':'Chanel'
    },
    {
        'tas':'Dior'
    },
    {
        'tas':'Papylon'
    },
    {
        'tas':'Hermes'
    },
    {
        'tas':'Louis Vuiton'
    },
    {
        'tas':'YVL'
    },
    {
        'tas':'Prada'
    },
    {
        'tas':'Gucci'
    },
    {
        'tas':'Givenchy'
    },
    {
        'tas':'Dolce&Gabbana'
    }
]
    return jsonify({'merek tas':merektas})  #will return the json

@app.route('/binatang/farhan', methods=['GET'])
def binatang():
    binatang = [
    {
        'nama':'Kucing',
        'Tempat':'Darat'
    },
    {
        'nama':'Anjing',
        'Tempat':'Darat'
    },
    {
        'nama':'Ikan',
        'Tempat':'Air'
    },
    {
        'nama':'Burung',
        'Tempat':'Darat/Udara'
    },
    {
        'nama':'Kijang',
        'Tempat':'Darat'
    },
    {
        'nama':'Kadal',
        'Tempat':'Darat'
    },
    {
        'nama':'Gajah',
        'Tempat':'Darat'
    },
    {
        'nama':'Jerapah',
        'Tempat':'Darat'
    },
    {
        'nama':'Hiu',
        'Tempat':'Air'
    },
    {
        'nama':'Badak',
        'Tempat':'Darat'
    },
    {
        'nama':'Gorila',
        'Tempat':'Darat'
    }
    ]
    return jsonify({'Binatang':binatang})

@app.route('/makanan/daerah', methods=['GET'])
def makanandaerah():
    makanandaerah = [
    {
        'Aceh':'Mie Aceh'
    },
    {
        'Medan':'Bika Ambon'
    },
    {
        'Padang':'Rendang Padang'
    },
    {
        'Jambi':'Gulai Ikan Patin Jambi'
    },
    {
        'Bengkulu':'Pendap Benngkulu'
    },
    {
        'Riau':'Gulai Belacan Riau'
    },
    {
        'Palembang':'empek empek Palembang'
    },
    {
        'Bangka':'Mie Bangka'
    },
    {
        'Lampung':'Seruit Lampung'
    },
    {
        'Jakarta':'Kerak Telor Jakarta'
    }
    ]
    return jsonify({'Makanan daerah di indonesia':makanandaerah}) 

@app.route('/minuman/soda', methods=['GET'])
def minumansoda():
    minumansoda = [
    {
        'soda':'Sprite'
    },
    {
        'soda':'fanta'
    },
    {
        'soda':'diet coke'
    },
    {
        'soda':'pepsi'
    },
    {
        'soda':'Aw'
    },
    {
        'soda':'Redbull'
    },
    {
        'soda':'Mocktail'
    },
    {
        'soda':'Squash'
    },
    {
        'soda':'Big Cola'
    },
    {
        'soda':'Coca Cola'
    }
    ]
    return jsonify({'minuman':minumansoda})

@app.route('/bandung/wisata', methods=['GET'])
def wisata():
    wisata = [
    {
        'wisata':'FarmHouse'
    },
    {
        'wisata':'The Loudge Maribaya'
    },
    {
        'wisata':'Puncak Bintang'
    },
    {
        'wisata':'Floating Market'
    },
    {
        'wisata':'Dusun Bambu'
    },
    {
        'wisata':'Dago Dream Park'
    },
    {
        'wisata':'Nu Art'
    },
    {
        'wisata':'Kawah Putih'
    },
    {
        'wisata':'Gunung Tangkuban Perahu'
    },
    {
        'wisata':'Kebun Teh'
    }
]

    return jsonify({'daftar wisata di bandung':wisata})

nama=[
    {
    'no':'21',
    'name':'Seta Permana',
    'hobi':'olahraga'
    },
    {
    'no':'22',
    'name':'Miftahul Hasanah',
    'hobi':'masak'
    }
]

@app.route('/club/Seta',methods=['GET'])
def getAllEmp():
    return jsonify({'data':nama})
    
@app.route('/input/daftarhargagame')
def daftarhargagame():
    game = "Daftar Harga Game"
    return gam

