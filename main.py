import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    functions.add_todo(todo=st.session_state["add_todo"])
    st.session_state["add_todo"] = ""

st.markdown("""
    <style>
        .stApp {
        background: url("https://cdn.discordapp.com/attachments/895045731793141771/1145823917643149323/2023_08_28_supra_night_1_blurred.png");
        background-size: cover;
        }
    </style>""", unsafe_allow_html=True)

st.title("Todo list App")

# Load todos as checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox: # gets checked
        todos.pop(index)
        functions.complete_todo(index)
        del st.session_state[f"{todo}_{index}"]
        st.experimental_rerun()


st.text_input("Add new todo", placeholder="Add new todo...",on_change=add_todo, key="add_todo", label_visibility="hidden")
