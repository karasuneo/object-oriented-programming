// データの初期表示
fetch("/address").then((response) => {
  console.log(response);
  response.json().then((data) => {
    console.log(data); // 取得されたレスポンスデータをデバッグ表示
    // データを表示させる
    show_data(data);
  });
});

const searchButton = document.querySelector("#search-submit");
searchButton.addEventListener("click", (ev) => {
  ev.preventDefault(); // HTMLが本来持っている正常なボタン処理をなかったことにする
  console.log("検索ボタン押されたよ");

  //   データ検索のWeb APIは/addressをGETメソッドで呼び出す
  // クエリパラメータにて、以下の項目を指定できます。
  // fn: 指定されたキーワードがFirst Nameに含まれるデータを返します。省略時全件。
  // ln: 指定されたキーワードがLast Nameに含まれるデータを返します。省略時全件。
  // em: 指定されたキーワードがEmailに含まれるデータを返します。省略時全件。

  // パラメータの取得を行う
  // <input type="text" id="search-firstname" placeholder="First name" name="fn" />
  const fn = document.querySelector("#search-firstname").value;
  // <input type="text" id="search-lastname" placeholder="Last name" name="ln" />
  const ln = document.querySelector("#search-lastname").value;
  // <input type="text" id="search-email" placeholder="Email address" name="em" />
  const em = document.querySelector("#search-email").value;

  const params = new URLSearchParams();

  if (fn && fn !== "") params.set("fn", fn);
  if (ln && ln !== "") params.set("ln", ln);
  if (em && em !== "") params.set("em", em);

  // 検索ごとに、<table id="address-list">〜</table>内の<tbody>〜</tbody>内部はクリアされて結果が表示される
  // データの初期表示
  fetch("/address?" + params.toString()).then((response) => {
    console.log(response);
    response.json().then((data) => {
      // console.log(data); // 取得されたレスポンスデータをデバッグ表示

      // データを表示させる
      const tableBody = document.querySelector("#address-list > tbody");
      tableBody.innerHTML = "";

      // レスポンスのJSONデータの件数が0だった場合
      if (data && data.length == 0) {
        let tr = document.createElement("tr");
        tr.innerHTML = "表示するデータがありません。";
        tableBody.appendChild(tr);
        return;
      }

      data.forEach((elm) => {
        let tr = document.createElement("tr");
        // first name
        let td = document.createElement("td");
        td.textContent = elm.first_name;
        tr.appendChild(td);
        // last name
        td = document.createElement("td");
        td.textContent = elm.last_name;
        tr.appendChild(td);
        // email
        td = document.createElement("td");
        td.textContent = elm.email;
        tr.appendChild(td);

        // 1行分をtableタグ内のtbodyへ追加する
        tableBody.appendChild(tr);
      });
    });
  });
});

const addButton = document.querySelector("#add-submit");
addButton.addEventListener("click", (e) => {
  // ボタンイベントのキャンセル
  e.preventDefault();

  // 入力チェック
  let fn = document.getElementById("add-firstname").value;
  let ln = document.getElementById("add-lastname").value;
  let em = document.getElementById("add-email").value;

  // 未入力がある項目ごとにエラーメッセージを積み上げる
  let error_message = "";
  if (!fn && fn === "") error_message += "first nameが未入力です。<br>";
  if (!ln && ln === "") error_message += "last nameが未入力です。<br>";
  if (!em && em === "") error_message += "emailが未入力です。<br>";

  // エラーメッセージがあるかどうかでエラーの表示有無を決定
  if (error_message !== "") {
    document.getElementById("error-container").innerHTML = error_message;
    document.getElementById("error-container").style.display = "block";
    return;
  } else {
    document.getElementById("error-container").innerHTML = "";
    document.getElementById("error-container").style.display = "none";
  }

  // データ送信
  let data = new FormData();
  data.append("fn", fn);
  data.append("ln", ln);
  data.append("em", em);

  fetch("/address", {
    method: "POST",
    body: data,
  }).then((response) => {
    // 入力項目の初期化
    document.getElementById("add").reset();

    // エラーの表示領域を初期化
    document.getElementById("error-container").innerHTML = "";
    document.getElementById("error-container").style.display = "none";
    // 登録メッセージ等の表示領域を初期化
    document.getElementById("message-container").innerHTML = "";
    document.getElementById("message-container").style.display = "none";

    // レスポンスデータからJSONを取り出し
    response.json().then((data) => {
      console.log(data.result);
      if (data.error) {
        // エラーの受信
        document.getElementById("error-container").innerHTML = data.error;
        document.getElementById("error-container").style.display = "block";
      } else if (data.result) {
        // メッセージの受信
        document.getElementById("message-container").innerHTML = data.result;
        document.getElementById("message-container").style.display = "block";
        if (data.json_data) {
          show_data(data.json_data);
        }
      }
    });
  });
});

// データ表示を関数化
const show_data = (data) => {
  // データを表示させる
  const tableBody = document.querySelector("#address-list > tbody");
  tableBody.innerHTML = "";

  // レスポンスのJSONデータの件数が0だった場合
  if (data && data.length == 0) {
    let tr = document.createElement("tr");
    tr.innerHTML = "表示するデータがありません。";
    tableBody.appendChild(tr);
    return;
  }

  data.forEach((elm) => {
    let tr = document.createElement("tr");
    // first name
    let td = document.createElement("td");
    td.textContent = elm.first_name;
    tr.appendChild(td);
    // last name
    td = document.createElement("td");
    td.textContent = elm.last_name;
    tr.appendChild(td);
    // email
    td = document.createElement("td");
    td.textContent = elm.email;
    tr.appendChild(td);

    // 1行分をtableタグ内のtbodyへ追加する
    tableBody.appendChild(tr);
  });
};
