import streamlit as st
import random

if "geheime_zahl" not in st.session_state:
    st.session_state["geheime_zahl"] = random.randint(1, 100)
if "versuche" not in st.session_state:
    st.session_state["versuche"] = 0

st.title("Zahlenraten-Spiel")

tipp = st.number_input("Gib eine Zahl zwischen 1 und 100 ein:", min_value=1, max_value=100, step=1)
if st.button("Überprüfen"):
    st.session_state["versuche"] += 1
    if tipp < st.session_state["geheime_zahl"]:
        st.warning("Zu niedrig!")
    elif tipp > st.session_state["geheime_zahl"]:
        st.warning("Zu hoch!")
    else:
        st.success(f"Richtig! In {st.session_state['versuche']} Versuchen erraten.")

if st.button("Nochmal spielen"):
    st.session_state["geheime_zahl"] = random.randint(1, 100)
    st.session_state["versuche"] = 0