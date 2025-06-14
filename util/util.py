import streamlit as st


def load_custom_css(file_path):
    """カスタムCSSファイルを読み込み、Streamlitに適用する"""
    try:
        with open(file_path, encoding="utf-8") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Error: CSS file not found at {file_path}")


def link(text, link, css_class="white-link-on-hover"):
    """スタイル付きの内部リンクを作成する"""
    st.markdown(
        f"""
        <a href="{link}" class="{css_class}">{text}</a>
        """,
        unsafe_allow_html=True
    )
