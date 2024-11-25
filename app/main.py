import streamlit as st

st.set_page_config(page_title="Cesta k financnej slobode!", page_icon="💰", layout="wide")


body = '<h1 style="text-align:center;">Cesta k financnej slobode! 💰</h1>'

st.markdown(body, unsafe_allow_html=True)


st.subheader("Zadajte Vaše údaje ✏️")

col1, col2, col3 = st.columns(3)

with col1:
    monthly_savings = st.number_input("Volná čiastka na investiciu (EUR)", value=100, step=50)
with col2:
    monthly_expenses = st.number_input("Mesačné náklady (EUR)", value=800, step=50)
with col3:
    current_savings = st.number_input("Začiatočná investícia (EUR)", value=1000, step=500)


st.subheader("Doplnujuce nastavenia ✏️")

with st.expander("Upraviť predpokladz výpočtu", expanded=True):
    col_add1, col_add2, col_add3 = st.columns(3)

    with col_add1:
        investment_return = st.slider("Očakávaný ročný výnos (%)", 1, 50, 8)
    with col_add2:
        inflation_rate = st.slider("Očakávaná ročná inflacia (%)", 0, 15, 3)
    with col_add3:
        safe_withdrawal_rate = st.slider("Očakávaný výnos investicie vo finančnej nezávislosti(%)", 1, 15, 4)