import streamlit_authenticator as stauth
hashed_password = stauth.Hasher(['abc']).generate()
print(hashed_password)

