import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    functions.add_todo(todo=st.session_state["add_todo"])
    st.session_state["add_todo"] = ""

st.title("Todo list App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.complete_todo(index)
        del st.session_state[f"{todo}_{index}"]
        st.rerun()


st.text_input("Add new todo", placeholder="Add new todo...",on_change=add_todo, key="add_todo", label_visibility="hidden")
