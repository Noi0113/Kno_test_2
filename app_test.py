import streamlit as st
def main():
    status_area = st.empty()
    
st.title('問題発見と解決テストサイト')
import pandas as pd

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

if __name__ == '__main__':
    main()
