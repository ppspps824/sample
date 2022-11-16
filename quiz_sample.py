import streamlit as st
from streamlit.components.v1 import html
import base64
import urllib.request
import time

# ページのタイトル設定
st.set_page_config(
    page_title="Wedding Quiz",
)

audio_placeholder = st.empty()

# セッション情報の初期化
if "page_id" not in st.session_state:
    st.session_state.page_id = "main"
    st.session_state.answers = []
    st.session_state.first = True

    audio_path1 = (
        "https://drive.google.com/uc?id=1pWcK--FaXhzv1q9TJkzPG54FcSNV_O_a"  # 入力する音声ファイル
    )

    audio_path2 = (
        "https://drive.google.com/uc?id=17VJPOVlWlzvwOWvvbFaXlxfMZ8LJJI2d"  # 入力する音声ファイル
    )

    with urllib.request.urlopen(url=audio_path1) as file1:
        contents = file1.read()

    audio_str1 = f"data:audio/ogg;base64,{base64.b64encode(contents).decode()}"
    st.session_state.audio_html1 = f"""
                    <audio autoplay=True>
                    <source src="{audio_str1}" type="audio/ogg" autoplay=True>
                    </audio>
                """
    with urllib.request.urlopen(url=audio_path2) as file2:
        contents = file2.read()
        audio_str2 = f"data:audio/ogg;base64,{base64.b64encode(contents).decode()}"

    st.session_state.audio_html2 = f"""
                    <audio autoplay=True>
                    <source src="{audio_str2}" type="audio/ogg" autoplay=True>
                    </audio>
                """


# 各種メニューの非表示設定
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# 最初のページ
def main():
    st.markdown(
        "<h1 style='text-align: center;'>💕💕Wedding Quiz💕💕</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(select)
        st.session_state.page_id = "page1"

    select = st.radio("テーブル番号を選んでね", ["A", "B", "C", "D", "E", "F", "G"])

    st.button("スタート！", on_click=change_page)


# 問題１
def page1():
    st.markdown(
        "<h1 style='text-align: center;'>第１問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(select)
        st.session_state.page_id = "page2"
        st.session_state.first = True

    select = st.radio("新郎の名前は？", ["たろう", "じろう", "さぶろう"])

    if not st.session_state.first:
        if select in ["たろう"]:
            audio_placeholder.empty()
            time.sleep(0.5)
            audio_placeholder.markdown(
                st.session_state.audio_html1, unsafe_allow_html=True
            )
        else:
            audio_placeholder.empty()
            time.sleep(0.5)
            audio_placeholder.markdown(
                st.session_state.audio_html2, unsafe_allow_html=True
            )

    st.session_state.first = False

    st.button("回答", on_click=change_page)


# 問題２
def page2():
    st.markdown(
        "<h1 style='text-align: center;'>第２問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(select)
        st.session_state.page_id = "page3"
        st.session_state.first = True

    select = st.radio("新婦の名前は？", ["はなこ", "ゆうこ", "うめこ"])

    if not st.session_state.first:
        if select in ["うめこ"]:
            audio_placeholder.empty()
            time.sleep(0.5)
            audio_placeholder.markdown(
                st.session_state.audio_html1, unsafe_allow_html=True
            )
        else:
            audio_placeholder.empty()
            time.sleep(0.5)
            audio_placeholder.markdown(
                st.session_state.audio_html2, unsafe_allow_html=True
            )

    st.session_state.first = False

    st.button("回答", on_click=change_page)


# 問題３
def page3():
    st.markdown(
        "<h1 style='text-align: center;'>第３問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(select)
        st.session_state.page_id = "page4"
        st.session_state.first = True

    select = st.radio("新郎の年齢は？", ["20歳", "30歳", "40歳", "50歳"])

    if not st.session_state.first:
        if select in ["40歳", "50歳"]:
            audio_placeholder.empty()
            time.sleep(0.5)
            audio_placeholder.markdown(
                st.session_state.audio_html1, unsafe_allow_html=True
            )
        else:
            audio_placeholder.empty()
            time.sleep(0.5)
            audio_placeholder.markdown(
                st.session_state.audio_html2, unsafe_allow_html=True
            )

    st.session_state.first = False

    st.button("回答", on_click=change_page)


# 問題４
def page4():
    st.markdown(
        "<h1 style='text-align: center;'>第４問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(select)
        st.session_state.page_id = "page5"
        st.session_state.first = True

    select = st.radio("新婦の年齢は？", ["20歳", "30歳", "40歳", "50歳"])

    if not st.session_state.first:
        if select in ["20歳", "30歳"]:
            audio_placeholder.empty()
            time.sleep(0.5)
            audio_placeholder.markdown(
                st.session_state.audio_html1, unsafe_allow_html=True
            )
        else:
            audio_placeholder.empty()
            time.sleep(0.5)
            audio_placeholder.markdown(
                st.session_state.audio_html2, unsafe_allow_html=True
            )

    st.session_state.first = False

    st.button("回答", on_click=change_page)


# 問題５
def page5():
    st.markdown(
        "<h1 style='text-align: center;'>第５問</h1>",
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(select)
        st.session_state.page_id = "page_end"
        st.session_state.first = True

    select = st.radio("２人の趣味は？", ["野球", "サッカー", "ピアノ", "卓球", "水泳"])

    if not st.session_state.first:
        if select in ["野球", "サッカー", "ピアノ"]:
            audio_placeholder.empty()
            time.sleep(0.5)
            audio_placeholder.markdown(
                st.session_state.audio_html1, unsafe_allow_html=True
            )
        else:
            audio_placeholder.empty()
            time.sleep(0.5)
            audio_placeholder.markdown(
                st.session_state.audio_html2, unsafe_allow_html=True
            )

    st.session_state.first = False
    st.button("回答", on_click=change_page)


# 最終ページ
def page_end():

    # 回答内容をサーバに送ったりなんなり

    st.markdown(
        "<h1 style='text-align: center;'>回答ありがとう🎉</h1>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(
        "<h2 style='text-align: center;'>あなたの回答</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='text-align: center;'>テーブル：{st.session_state.answers[0]}</div>",
        unsafe_allow_html=True,
    )
    for num, value in enumerate(st.session_state.answers, 0):
        if num != 0:
            st.markdown(
                f"<div style='text-align: center;'>第{num}問：{value}</div>",
                unsafe_allow_html=True,
            )
    ## バルーンを飛ばす!
    st.balloons()


# ページ遷移のための判定
if st.session_state.page_id == "main":
    main()

if st.session_state.page_id == "page1":
    page1()

if st.session_state.page_id == "page2":
    page2()

if st.session_state.page_id == "page3":
    page3()

if st.session_state.page_id == "page4":
    page4()

if st.session_state.page_id == "page5":
    page5()

if st.session_state.page_id == "page_end":
    page_end()
