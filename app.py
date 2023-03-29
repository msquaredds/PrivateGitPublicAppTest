"""
Test to see if we can have a public repository with a private section,
which can be accessed by the streamlit app if a user's credentials are
correct.
"""

import os
import streamlit as st

from git import Repo


def main():
    st.markdown("# This section is public!")

    password = st.text_input(
        "Enter your password to see the private section.",
        help="This is just a test, so the correct password is 'password'.")

    if password == 'password':
        st.write("You have the correct password!")
        if not os.path.exists('./private'):
            git_pat = st.secrets['GIT_PAT']
            repo_name = "https://msquaredds:" + git_pat +\
                        "@github.com/msquaredds/PrivateGitForPublicApp.git"
            Repo.clone_from(repo_name, "./private")
        print(os.path.abspath(os.getcwd()))



if __name__ == '__main__':
    main()
