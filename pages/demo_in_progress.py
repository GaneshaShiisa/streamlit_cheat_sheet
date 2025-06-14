import streamlit as st
import time

# Display media
st.header("Demo in progress", anchor="demo-in-progress")

if st.button("処理中デモ１"):
    with st.status("計算を開始します...", expanded=True) as status:
        for i in range(5):
            st.write(f"{i+1} 秒目の処理中...")
            time.sleep(1)
        status.update(label="計算が完了しました ✅", state="complete")

if st.button("処理中デモ２"):
    progress = st.progress(0)
    status_text = st.empty()

    for i in range(100):
        status_text.text(f"処理中... {i+1}%")
        progress.progress(i + 1)
        time.sleep(0.05)

if st.button("処理中デモ３"):
    placeholder = st.empty()

    for i in range(5):
        placeholder.text(f"ステップ {i+1} 実行中...")
        time.sleep(1)

    placeholder.text("すべての処理が完了しました ✅")

if st.button("処理中デモ４"):
    with st.spinner("計算中です...しばらくお待ちください"):
        time.sleep(5)

    st.success("計算が完了しました！")
