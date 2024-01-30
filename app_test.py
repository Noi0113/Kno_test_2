import streamlit as st

#######トップページ

import sqlite3
import hashlib
import pandas as pd

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

#sqliteに接続
conn = sqlite3.connect('user_database.db')
c=conn.cursor()

#パスワードのハッシュ化
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

#機能の追加

menu = ["ホーム", "ログイン", "サインアップ"]
choice = st.sidebar.selectbox("メニュー", menu)

if choice == "ホーム":
	st.subheader("ホーム画面です")
elif choice == "ログイン":
	st.subheader("ログイン画面です")

	username = st.sidebar.text_input("ユーザー名を入力してください")
	password = st.sidebar.text_input("パスワードを入力してください", type='password')
	if st.sidebar.checkbox("ログイン"):
		hashed_pswd = make_hashes(password)
		result = login_user(username, check_hashes(password, hashed_pswd))
    		if result:
	    		st.success("{}さんでログインしました".format(username))
    		else:
	    		st.warning("ユーザー名かパスワードが間違っています")

elif choice == "サインアップ":
	st.subheader("新しいアカウントを作成します")
	new_user = st.text_input("ユーザー名を入力してください")
	new_password = st.text_input("パスワードを入力してください", type='password')

	if st.button("サインアップ"):
    		create_user()
    		add_user(new_user, make_hashes(new_password))
    		st.success("アカウントの作成に成功しました")
    		st.info("ログイン画面からログインしてください")


#######トップページ終わり

#######新規作成クリック後のページ
def new():
    st.sidebar.title("ページが切り替わりました")
    st.markdown("## 次のページです")

if __name__ == '__main__':
    main()
