import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)


st.title("My Todo App")
st.subheader("Hello everybody")
st.write("Today is the most productive day in my life")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo")
