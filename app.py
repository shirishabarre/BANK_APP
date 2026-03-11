import streamlit as st

# ---------- Custom CSS ----------
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}

.title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#1f4e79;
}

.card {
    padding:20px;
    border-radius:10px;
    background-color:white;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Bank Class ----------
class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return f"Transaction Successful. Collected ₹{amount}"
        else:
            return "Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit Successful. Total Balance: ₹{self.balance}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"Mobile number updated: {self.mobile_number}"

    def check_balance(self):
        return f"Total Account Balance: ₹{self.balance}"

# ---------- Title ----------
st.markdown('<p class="title">🏦 SBI Digital Bank</p>', unsafe_allow_html=True)

# Session
if "account" not in st.session_state:
    st.session_state.account = None

# Sidebar
menu = ["Create Account","Deposit","Withdraw","Check Balance","Update Mobile"]
choice = st.sidebar.selectbox("📋 Menu", menu)

# ---------- Create Account ----------
if choice == "Create Account":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1,col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age",min_value=18)

    with col2:
        acc = st.text_input("Account Number")
        mobile = st.text_input("Mobile Number")

    balance = st.number_input("Initial Balance")

    if st.button("Create Account"):
        st.session_state.account = BankApplication(name,acc,age,mobile,balance)
        st.success("✅ Account Created Successfully")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Deposit ----------
elif choice == "Deposit":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if st.session_state.account:

        amount = st.number_input("Enter Deposit Amount")

        if st.button("Deposit Money"):
            result = st.session_state.account.deposit(amount)
            st.success(result)

    else:
        st.warning("Please create account first")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Withdraw ----------
elif choice == "Withdraw":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if st.session_state.account:

        amount = st.number_input("Enter Withdraw Amount")

        if st.button("Withdraw Money"):
            result = st.session_state.account.withdraw(amount)
            st.info(result)

    else:
        st.warning("Please create account first")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Balance ----------
elif choice == "Check Balance":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if st.session_state.account:

        balance = st.session_state.account.check_balance()

        st.metric(
            label="💰 Account Balance",
            value=balance
        )

    else:
        st.warning("Please create account first")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Update Mobile ----------
elif choice == "Update Mobile":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if st.session_state.account:

        new_mobile = st.text_input("Enter New Mobile Number")

        if st.button("Update Number"):
            result = st.session_state.account.update_mobile(new_mobile)
            st.success(result)

    else:
        st.warning("Please create account first")

    st.markdown('</div>', unsafe_allow_html=True)