import streamlit as st

#######トップページ
def main():
    status_area = st.empty()
#タイトル
st.title('問題発見と解決テストサイト') 

#CSVファイル読み込み
import pandas as pd
uploaded_file = st.file_uploader("CSVファイルを選択してください(まだファイルアップロードする場所を作っただけで、アップロードしても何も起こらないです)", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

#ボタン
st.button('新規作成',use_container_width=True)
st.button('対戦表の確認',use_container_width=True,help='ページ準備中')


#######トップページ終わり

#######新規作成クリック後のページ
def new():
    st.sidebar.title("ページが切り替わりました")
    st.markdown("## 次のページです")

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()
