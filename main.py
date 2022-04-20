import requests
from flask import Flask, render_template


n_point_api = 'https://api.npoint.io/3c8daaf5ee16527ac225'

app = Flask(__name__)



id_list = []
title_list = []
subtitle_list = []
text_body_list = []
datum_list = []
title = ''
sub_title = ''
datum = ''
body = ''

@app.route('/')
def main():
    api_data = requests.get(n_point_api).json()
    # for data in api_data:
    #     id_list.append(data['id'])
    #     title_list.append(data['title'])
    #     subtitle_list.append(data['subtitle'])
    #     text_body_list.append(data['body'])
    #     datum_list.append(data['datum'])

    return render_template('index.html', api_data=api_data)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/post.html/<blod_id>')
def post(blod_id):
    global title, sub_title, datum, body
    api_data = requests.get(n_point_api).json()
    for data in api_data:
        id_list.append(data['id'])
        title_list.append(data['title'])
        subtitle_list.append(data['subtitle'])
        text_body_list.append(data['body'])
        datum_list.append(data['datum'])
    for item in range(3):
        if id_list[item] == int(blod_id):
            title = title_list[item]
            sub_title = subtitle_list[item]
            datum = datum_list[item]
            body = text_body_list[item]

    return render_template('post.html',body=body, blod_id=blod_id, title=title, sub_title=sub_title, datum=datum, id_list=id_list)


if __name__ == '__main__':
    app.run(debug=True)
    about()
    contact()
    post()
    main()
