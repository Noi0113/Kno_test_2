import streamlit as st
import sqlite3
import hashlib
import pandas as pd

#ここからサイトの構造
def main():
    status_area = st.empty()
#タイトル
st.title('競技かるた　対戦表作成サイト') 


#ボタン
st.link_button('新規作成',"https://monketsu-newcreate.streamlit.app/",use_container_width=True)
st.link_button('アンケート回答',"https://monketsu-questionnaire.streamlit.app/",use_container_width=True)
st.link_button('対戦表の確認',"https://monketsu-2ndpage.streamlit.app/",use_container_width=True)

st.subheader('このサイトの使い方')
st.markdown('1：新規作成'\n'大会主催者は大会IDとパスワードを作成し、参加者に共有してください')
st.markdown('2:アンケート回答')
st.markdown('大会参加者は大会IDとパスワードでログインし、個人の情報を入力してください')
st.markdown('3:対戦表の確認')
st.markdown('個人アンケートの入力終了後、大会参加者は大会IDとパスワードを入力し、対戦表を作成してください')

#######トップページ終わり

#######新規作成クリック後のページ
def new():
    st.sidebar.title("ページが切り替わりました")
    st.markdown("## 次のページです")

if __name__ == '__main__':
    main()
