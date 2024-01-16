import time

import streamlit as st


def main():
    status_area = st.empty()

    # カウントダウン
    count_down_sec = 5
    for i in range(count_down_sec):
        # プレースホルダーに残り秒数を書き込む
        status_area.write(f'{count_down_sec - i} sec left')
        # スリープ処理を入れる
        time.sleep(1)

    # 完了したときの表示
    status_area.write('Done!')
    # 風船飛ばす
    st.balloons()


if __name__ == '__main__':
    main()
