import streamlit as st
def main():
    status_area = st.empty()
 #ここから上は編集しない

#タイトル
st.title('問題発見と解決テストサイト')


#CSVファイルをアップロード(とりあえず)
import pandas as pd
uploaded_file = st.file_uploader("CSVファイルを選択してください//(まだファイルアップロードする場所を作っただけで、アップロードしても何も起こらないです。今後最適化を実験するときのために使えるかも)", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

#ボタン
st.button('新規作成',use_container_width=True)
st.button('対戦表の確認',help='作成中のため機能無')


#ここから下は編集しない
if __name__ == '__main__':
    main()
