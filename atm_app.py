import streamlit as st

# Initialize session state for balance
if 'balance' not in st.session_state:
    st.session_state.balance = 1000  # Starting balance

st.title("💳 ATM Simulator")

# Display current balance
st.subheader(f"Current Balance: ₹{st.session_state.balance}")

# Select operation
operation = st.selectbox("Choose an operation", ["Deposit", "Withdraw", "Check Balance"])

# Deposit
if operation == "Deposit":
    amount = st.number_input("Enter amount to deposit", min_value=1)
    if st.button("Deposit"):
        st.session_state.balance += amount
        st.success(f"₹{amount} deposited successfully!")

# Withdraw
elif operation == "Withdraw":
    amount = st.number_input("Enter amount to withdraw", min_value=1)
    if st.button("Withdraw"):
        if amount <= st.session_state.balance:
            st.session_state.balance -= amount
            st.success(f"₹{amount} withdrawn successfully!")
        else:
            st.error("Insufficient balance!")

# Check Balance
elif operation == "Check Balance":
    st.info(f"Your current balance is ₹{st.session_state.balance}")

# Footer
st.markdown("---")
st.caption("This is a basic ATM simulation built with Streamlit.")