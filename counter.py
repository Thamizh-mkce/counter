import streamlit as st

# Initialize session state variables
if 'counter' not in st.session_state:
    st.session_state.counter = 0
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to update counter and history
def update_counter(change):
    st.session_state.counter += change
    st.session_state.history.append(st.session_state.counter)

# Streamlit app layout
st.title("Enhanced Counter")

# Input fields for custom increment and decrement values
increment_value = st.number_input("Increment value", min_value=1, value=1, step=1)
decrement_value = st.number_input("Decrement value", min_value=1, value=1, step=1)

# Input fields for maximum and minimum counter values
min_value = st.number_input("Minimum counter value", value=-100)
max_value = st.number_input("Maximum counter value", value=100)

# Ensure the counter stays within specified bounds
if st.session_state.counter < min_value:
    st.session_state.counter = min_value
if st.session_state.counter > max_value:
    st.session_state.counter = max_value

# Display the current counter value
st.write(f"Counter value: {st.session_state.counter}")

# Buttons to increment and decrement the counter
col1, col2 = st.columns(2)
with col1:
    if st.button("Increment"):
        if st.session_state.counter + increment_value <= max_value:
            update_counter(increment_value)
        else:
            st.warning("Counter exceeds maximum value!")
with col2:
    if st.button("Decrement"):
        if st.session_state.counter - decrement_value >= min_value:
            update_counter(-decrement_value)
        else:
            st.warning("Counter below minimum value!")

# Reset button to reset the counter and clear history
if st.button("Reset"):
    st.session_state.counter = 0
    st.session_state.history = []

# Display counter history
st.subheader("Counter History")
st.write(st.session_state.history)
