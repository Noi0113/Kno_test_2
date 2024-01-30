import streamlit as st
import sqlite3
import hashlib
import pandas as pd

#ここからサイトの構造
def main():
    status_area = st.empty()
#タイトル
st.title('問題発見と解決テストサイト') 


#ボタン
st.link_button('新規作成',"https://monketsu-newcreate.streamlit.app/",use_container_width=True)
st.link_button('アンケート回答',"https://monketsu-questionnaire.streamlit.app/",use_container_width=True)
st.link_button('対戦表の確認',"https://monketsu-2ndpage.streamlit.app/",use_container_width=True)


##ログインについて
#st.link_button()を導入したい


#######トップページ終わり

#######新規作成クリック後のページ
def new():
    st.sidebar.title("ページが切り替わりました")
    st.markdown("## 次のページです")

if __name__ == '__main__':
    main()
