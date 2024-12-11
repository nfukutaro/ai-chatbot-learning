import streamlit as st
st.title("初めてのAIチャットボット")

#チャット履歴がなければ初期化
#st.session_state に chat_history というキーが存在するかどうかをチェック
if "chat_history" not in st.session_state:
    #なければ、新しく空のリストをつくることで初期化をしている
    st.session_state.chat_history = []

#チャット履歴を表示
#st.session_state.chat_history に保存されているチャットメッセージを1つずつループで取り出す
for message in st.session_state.chat_history:
    #Streamlitの chat_message コンテキストマネージャを使用して、チャットメッセージを表示するためのコード
    #message["role"] には、メッセージの発信者の役割（例えば、"user" や "assistant"）が含まれる。これを使ってメッセージのスタイルを決定
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#チャットボットの返事を作成
def generate_response(user_input):
    if "こんにちは" in user_input:
        return "こんにちは！今日もいい天気ですね"
    elif "ありがとう" in user_input:
        return "どうもおおきに"
    else:
        return f"ご質問ありがとうございます。『{user_input}』についてはお答えできないです。"

#ユーザの入力が送信された際に実行される処理
if prompt:= st.chat_input("何かお困りですか？"):
    #ユーザの入力を表示
    with st.chat_message("user"):
        st.markdown(prompt)
    #ユーザの入力をチャット履歴に追加
    st.session_state.chat_history.append({"role":"user","content":prompt})
    
    #チャットボットの返事を表示
    resopnse = generate_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(resopnse)
    #チャットボットの返事をチャット履歴に追加
    st.session_state.chat_history.append({"role":"assistant","content":resopnse})