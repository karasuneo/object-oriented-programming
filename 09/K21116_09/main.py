from flask import Flask, request, render_template, jsonify
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/address
@app.route('/address', methods=["GET"])
def address_get():

      # 検索パラメータの取得
      p_first_name = request.args.get('fn', None)
      p_last_name = request.args.get('ln', None)
      p_email = request.args.get('em', None)

      with open('address.json') as f:
            json_data = json.load(f)

      # パラメータにより返すデータをフィルタリングする
      if p_first_name is not None:
            json_data = list(filter(lambda item: p_first_name.lower() in item["first_name"].lower(), json_data))
      if p_last_name is not None:
            json_data = list(filter(lambda item: p_last_name.lower() in item["last_name"].lower(), json_data))
      if p_email is not None:
            json_data = list(filter(lambda item: p_email.lower() in item["email"].lower(), json_data))

      return jsonify(json_data)

# データの登録
# http://127.0.0.1:5000/address
@app.route('/address', methods=["POST"])
def address_set():

      first_name = request.form.get('fn')
      last_name = request.form.get('ln')
      email = request.form.get('em')

      add_address = {"email": email, "first_name": first_name, "last_name": last_name}

      with open('address.json') as f:
            try:
                  json_data = json.load(f)
            except ValueError:
                  json_error = {'error': "問題が起こりました"}
                  return json_error 
      json_data.append(add_address)

      with open('address.json', 'w') as f:
            try:
                  json.dump(json_data, f)
            except ValueError:
                  json_error = {'error': "問題が起こりました"}
                  return json_error
            
      
      return jsonify(json_data)

# データの表示
# http://127.0.0.1:5000/
@app.route('/')
def index():
      return render_template("addressbook.html")

if __name__ == "__main__":
      # debugモードが不要の場合は、debug=Trueを消してください
      app.run(debug=True)