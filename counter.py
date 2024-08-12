import streamlit as st

# Initialize session state for the counter if it doesn't exist
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Function to increment the counter
def increment():
    st.session_state.counter += 1

# Function to decrement the counter
def decrement():
    st.session_state.counter -= 1

# Streamlit app layout
st.title("Simple Counter")

# Display the current counter value
st.write(f"Counter value: {st.session_state.counter}")

# Buttons to increment and decrement the counter
col1, col2 = st.columns(2)
with col1:
    st.button("Increment", on_click=increment)
with col2:
    st.button("Decrement", on_click=decrement)

# Optionally, add a reset button
if st.button("Reset"):
    st.session_state.counter = 0
