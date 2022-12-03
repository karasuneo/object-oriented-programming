// データの初期表示
fetch("/address").then((response) => {
  console.log(response);
  response.json().then((data) => {
    console.log(data); // 取得されたレスポンスデータをデバッグ表示
    // データを表示させる
    const tableBody = document.querySelector("#address-list > tbody");
    data.forEach((elm) => {
      // 1行づつ処理を行う
      let tr = document.createElement("tr");
      // first name
      let td = document.createElement("td");
      td.innerText = elm.first_name;
      tr.appendChild(td);
      // last name
      td = document.createElement("td");
      td.innerText = elm.last_name;
      tr.appendChild(td);
      // email
      td = document.createElement("td");
      td.innerText = elm.email;
      tr.appendChild(td);

      // 1行分をtableタグ内のtbodyへ追加する
      tableBody.appendChild(tr);
    });
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
