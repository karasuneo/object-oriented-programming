from flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ

app = Flask(__name__)

# 1. プロジェクトのトップ（じゃんけんアプリや、課題のアプリへのリンクを配置するだけ）
@app.route('/')
def index():
      return render_template('index.html')


# 2. じゃんけんアプリ, 占いアプリの入力フォーム
@app.route('/janken')
def janken():
      # じゃんけんの入力画面のテンプレートを呼び出し
      return render_template('janken_form.html')

@app.route('/uranai')
def uranai():
      # 占いの入力画面のテンプレートを呼び出し
      return render_template('uranai_form.html')


# 3. じゃんけんデータ送信先とじゃんけん結果表示画面
@app.route('/janken/play', methods=["POST"])
@app.route('/uranai/play', methods=["POST"])
def janken_play():
      # <input type="text" id="your_name" name="name">
      name = request.form.get("name")
      if not name:
            name = "名無しさん"

      # <input type="checkbox" id="settai_mode" value="settai" name="mode" />
      mode = request.form.get("mode")
      if not mode:
            mode = "standard"
      print(mode)
      
      # <input type="radio" id="hand_rock" value="rock" name="hand">
      # <input type="radio" id="hand_scissor" value="scissor" name="hand">
      # <input type="radio" id="hand_paper" value="paper" name="hand">
      hand = request.form.get("hand", None)
      
      # リストの中からランダムに選ぶ
      cpu = random.choice(["rock", "scissor", "paper"])
      
      if mode == "standard":
            # じゃんけん処理
            if hand == cpu:
                  result_message = "あいこ"
            else:
                  if hand == "rock":
                        if cpu == "scissor":
                              result_message = "{}の勝ち".format(name)
                        else:
                              result_message = "{}の負け".format(name)
                  elif hand == "scissor":
                        if cpu == "paper":
                              result_message = "{}の勝ち".format(name)
                        else:
                              result_message = "{}の負け".format(name)
                  elif hand == "paper":
                        if cpu == "rock":
                              result_message = "{}の勝ち".format(name)
                        else:
                              result_message = "{}の負け".format(name)
                  else:
                        result_message = "後出しはダメです。"

      elif mode == "settai":
            # じゃんけん処理
            if hand == "rock":
                  cpu = "scissor"
                  result_message = "{}の勝ち".format(name)
            elif hand == "scissor":
                  cpu = "paper"
                  result_message = "{}の勝ち".format(name)
            elif hand == "paper":
                  cpu = "rock"
                  result_message = "{}の勝ち".format(name)
            else:
                  hand = "rock"
                  cpu = "scissor"
                  result_message = "{}の勝ち".format(name)

      # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
      return render_template('janken_play.html',
            result_message=result_message,
            name=name,
            hand=hand,
            cpu=cpu)

def uranai_play():
      # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
      return render_template('uranai_play.html')

if __name__ == '__main__':
      app.run(debug=True)