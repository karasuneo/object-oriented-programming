from flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ
import datetime # 現在日時取得のライブラリ

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

def janken_play():
      # <input type="text" id="your_name" name="name">
      name = request.form.get("name")
      if not name:
            name = "名無しさん"

      # <input type="checkbox" id="settai_mode" value="settai" name="mode" />
      mode = request.form.get("mode")
      if not mode:
            mode = "standard"
      
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

@app.route('/uranai/result', methods=["POST"])

def uranai_result():
      # 現在日時を取得するメソッドの定義
      dt_now = datetime.datetime.now()
      
      # htmlから受け取った値をパース
      name = request.form.get("name")
      birthday = request.form.get("birthday")
      
      # 生年月日が未入力またが名前が未入力の時入力不備で占えませんでしたとする
      if not name or not birthday:
            result = 1
            result_message = "入力不備で占えませんでした"
            
            return render_template('uranai_result.html',
            result=result,
            result_message=result_message,
            )

      # 現在日付をyyyyMMdd形式で数値化する
      birthday_num = birthday.replace('-', '')
      
      # 生年月日をyyyyMMdd形式で数値化するç
      currentday_num = str(dt_now.year) + str(dt_now.month) + str(dt_now.day)
      
      # 数値化した現在日付から生年月日を減算し、結果の絶対値を算出する
      date_diff = abs(int(birthday_num) - int(currentday_num))
      
      #「減算結果の絶対値」と「名前の文字数」を掛け算にて算出する
      pro = date_diff * len(name)
      
      #「掛け算結果を5で割った余り」をList:[5, 1, 3, 2, 4]のインデックスとして使用し取り出した数値要素を占い結果とする
      result_list = [5, 1, 3, 2, 4]
      rem = pro % 5
      result = result_list[rem]
      
      # 1〜5の数値で得られる5段階の占い結果に対して、それぞれ各段階における適当なメッセージも添えること
      if result == 1:
            result_message = "すごく不幸だね"
      elif result == 2:
            result_message = "不幸だね"
      elif result == 3:
            result_message = "普通だね"
      elif result == 4:
            result_message = "幸運だね"
      elif result == 5:
            result_message = "すごく幸運だね"

      # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
      return render_template('uranai_result.html',
            result=result,
            result_message=result_message,
            )

if __name__ == '__main__':
      app.run(debug=True)