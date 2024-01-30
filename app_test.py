import streamlit as st
import sqlite3
import hashlib
import pandas as pd


#ここまでログイン機能について

#ここからサイトの構造
def main():
    status_area = st.empty()
#タイトル
st.title('問題発見と解決テストサイト') 

#CSVファイル読み込み
#import pandas as pd
#uploaded_file = st.file_uploader("CSVファイルを選択してください(まだファイルアップロードする場所を作っただけで、アップロードしても何も起こらないです)", type="csv")
#if uploaded_file is not None:
#    data = pd.read_csv(uploaded_file)

#ボタン
st.link_button('新規作成',"https://monketsu-2ndpage.streamlit.app/",use_container_width=True)
st.button('対戦表の確認',use_container_width=True,help='ページ準備中')
st.button('送信')

##ログインについて
#st.link_button()を導入したい

#機能の追加
#ここからログイン機能について必要な定義
#sqliteに接続
conn = sqlite3.connect('user_database.db')
c=conn.cursor()

def create_user():
    c.execute('CREATE TABLE IF NOT EXISTS userstable (username TEXT PRIMARY KEY, password TEXT)')

def add_user(username, password):
    # ユーザーが既に存在するかを確認
    c.execute('SELECT * FROM userstable WHERE username = ?', (username,))
    existing_user = c.fetchone()
    if existing_user:
        return True
    else:
	    c.execute('INSERT INTO userstable (username, password) VALUES (?, ?)', (username, password))
	    conn.commit()
	    return False

def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchall()
    return data

#パスワードのハッシュ化
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# ページの選択と表示
menu = ["大会ログイン", "新規大会登録" ]
choice = st.selectbox("選択してください",menu)
st.write("{}ページです".format(choice))

if choice == "大会ログイン":
	username = st.text_input("大会名を入力")
	password = st.text_input("大会パスワードを入力してください",type='password')
	if st.button('ログイン'):
		hashed_pswd = make_hashes(password)
		result = login_user(username,check_hashes(password,hashed_pswd))
		if result:
			st.success("大会名：{}でログインしました".format(username))
		else:
			st.warning("大会名か大会パスワードが間違っています")

elif choice == "新規大会登録":
	new_user = st.text_input("大会名を入力してください（被りがあると注意されて新規作成できない予定）")
	new_password = st.text_input("大会パスワードを入力してください",type='password')
	if st.button("登録"):
		if add_user(new_user,make_hashes(new_password)):
			st.warning("その大会名は既にしようされています")
		else:
			create_user()
			st.success("新しい大会の作成に成功しました")
			st.info("大会ログイン画面からログインしてください")


#######トップページ終わり

#######新規作成クリック後のページ
def new():
    st.sidebar.title("ページが切り替わりました")
    st.markdown("## 次のページです")

if __name__ == '__main__':
    main()
