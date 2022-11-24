from flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ

app = Flask(__name__)

# 1. プロジェクトのトップ（じゃんけんアプリや、課題のアプリへのリンクを配置するだけ）
@app.route('/')
def index():
      return render_template('index.html')


# 2. じゃんけんアプリの入力フォーム
@app.route('/janken')
def janken():
      # じゃんけんの入力画面のテンプレートを呼び出し
      return render_template('janken_form.html')


# 3. じゃんけんデータ送信先とじゃんけん結果表示画面
@app.route('/janken/play', methods=["POST"])
def janken_play():
      pass # 関数の中身を空にできないので、pass構文を使って埋めてます


if __name__ == '__main__':
      app.run(debug=True)