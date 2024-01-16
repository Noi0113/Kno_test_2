import streamlit as st
def main():
    status_area = st.empty()
 #ここから上は編集しない

#タイトル
st.title('問題発見と解決テストサイト')


#CSVファイルをアップロード(とりあえず)
import pandas as pd
uploaded_file = st.file_uploader("CSVファイルを選択してください", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)


#ここから下は編集しない
if __name__ == '__main__':
    main()
