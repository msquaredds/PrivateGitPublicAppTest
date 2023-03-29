"""
Test to see if we can have a public repository with a private section,
which can be accessed by the streamlit app if a user's credentials are
correct.
"""

import streamlit as st


def main():
    st.markdown("# This section is public!")

    password = st.text_input(
        "Enter your password to see the private section.",
        help="This is just a test, so the correct password is 'password'.")

    if password == 'password':
        st.markdown("# This section is private!")


if __name__ == '__main__':
    main()
