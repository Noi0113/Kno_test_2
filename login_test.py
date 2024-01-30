import streamlit as st
import hashlib
import pandas as pd
import sqlite3

menu = ["ホーム", "大会ログイン", "新規大会登録"]
choice = st.sidebar.selectbox("メニュー", menu)

if choice == "ホーム":
	st.subheader("ホーム画面です")
elif choice == "大会ログイン":
	st.subheader("大会ログイン画面です")

	username = st.sidebar.text_input("大会名を入力してください")
	password = st.sidebar.text_input("大会パスワードを入力してください", type='password')
	if st.sidebar.checkbox("ログイン"):
		hashed_pswd = make_hashes(password)
		result = login_user(username, check_hashes(password, hashed_pswd))
		if result:
			st.success("大会名：{}でログインしました".format(username))
		else:
	    		st.warning("大会名か大会パスワードが間違っています")

elif choice == "新規大会登録":
	st.subheader("新しい大会を作成します")
	new_user = st.text_input("大会名を入力してください（被りがあると注意されます）")
	new_password = st.text_input("大会パスワードを入力してください", type='password')

	if st.button("登録"):
    		create_user()
    		add_user(new_user, make_hashes(new_password))
    		st.success("新しい大会の作成に成功しました")
    		st.info("大会ログイン画面からログインしてください")
