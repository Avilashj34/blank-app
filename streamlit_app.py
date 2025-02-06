import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


st.title("📊 SMS Cost Analysis Dashboard")
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])


st.success("Data vendor")
