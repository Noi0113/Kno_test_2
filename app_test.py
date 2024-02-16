import streamlit as st

#ここからサイトの構造
def main():
    status_area = st.empty()
#タイトル
    st.title('競技かるた　対戦表作成サイト') 
    st.markdown('') #空行の作成

    st.subheader('このサイトの使い方')
    st.markdown('①新規作成')
    st.markdown('大会主催者が大会名とパスワード、その他必要情報を入力してください。')
    st.link_button('新規作成',"https://monketsu-newcreate.streamlit.app/",use_container_width=True)
    st.markdown('') #空行の作成

    st.markdown('②アンケート回答')
    st.markdown('大会参加者は、大会主催者から共有された大会名とパスワードを用いて、自分の情報を入力してください')
    st.link_button('アンケート回答',"https://monketsu-questionnaire.streamlit.app/",use_container_width=True)
    st.markdown('') #空行の作成

    st.markdown('③対戦表の確認')
    st.markdown('大会主催者が、大会参加者がアンケートを入力した後に大会名とパスワードを入力することで')
    st.markdown('対戦表が確認できます')
    st.link_button('対戦表の確認',"https://monketsu-2ndpage.streamlit.app/",use_container_width=True)
    st.markdown('') #空行の作成
#ボタン

#######トップページ終わり

#######新規作成クリック後のページ
def new():
    st.sidebar.title("ページが切り替わりました")
    st.markdown("## 次のページです")

if __name__ == '__main__':
    main()
