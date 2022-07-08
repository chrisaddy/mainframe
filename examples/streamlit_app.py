import streamlit as st


def main_page():
    st.markdown("ENTER THE MAINFRAME")
    st.sidebar.markdown("# HOME")


def t_test():
    st.markdown("# T-Test")
    st.sidebar.markdown("# T-test stuff")


page_names_to_funcs = {
    "Home": main_page,
    "T-Test": t_test,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
