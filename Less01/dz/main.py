from flask import Flask, render_template

app = Flask(__name__)


# Определение маршрутов
@app.route('/')
@app.route('/clothes/')
def clothes():
    ttl = 'Одежда'
    stre = [{'name': 'Рубашка REUS, размер L, черный',
              'src': "https://avatars.mds.yandex.net/get-mpic/4867510/img_id4959916288646721091.png/600x800",
              "price": "5555"},
            {'name': 'Майка Inferno Style, размер L, оранжевый',
             'src': "https://avatars.mds.yandex.net/get-mpic/11378054/2a0000018b67c5bb4c3916327a5c48173081/600x800",
             "price": "5555"}
            ]

    return render_template('clothes.html', title=ttl, store=stre)


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')


if __name__ == '__main__':
    app.run(debug=True)
