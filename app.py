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
        # See if the password is generally correct
        st.write("You have the correct password!")

        # Get the private directory if it doesn't already exist
        if not os.path.exists('./private'):
            git_pat = st.secrets['GIT_PAT']
            repo_name = "https://msquaredds:" + git_pat +\
                        "@github.com/msquaredds/PrivateGitForPublicApp.git"
            Repo.clone_from(repo_name, "./private")
        #st.write("Directory:")
        #st.write(os.listdir(os.path.abspath(os.getcwd())))
        # Import the private code
        from private import main
        st.markdown(main.private_text)

        # Do the same with a private directory
        if not os.path.exists('./private_dir'):
            git_pat = st.secrets['GIT_PAT']
            # This is a more specific directory within a repo
            repo_name = "https://msquaredds:" + git_pat +\
                        "@github.com/msquaredds/" +\
                        "PrivateGitForPublicApp/tree/main/private_dir"
            Repo.clone_from(repo_name, "./private_dir")
        st.write("Directory:")
        st.write(os.listdir(os.path.abspath(os.getcwd())))
        # Import the private code
        import private_dir
        private_dir.test.say_hi()



if __name__ == '__main__':
    main()
