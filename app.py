"""
Test to see if we can have a public repository with a private section,
which can be accessed by the streamlit app if a user's credentials are
correct.
"""

import os
import shutil
import streamlit as st

from git import Repo
from pathlib import Path


def main():
    st.markdown("# This section is public!")

    password = st.text_input(
        "Enter your password to see the private section.",
        help="This is just a test, so the correct password is 'password'.")

    if password == 'password':
        # See if the password is generally correct
        st.write("You have the correct password!")

        # Show the directory
        st.write("Directory:")
        st.write(os.listdir(os.path.abspath(os.getcwd())))

        # Get the private directory if it doesn't already exist
        if not os.path.exists('./private'):
            git_pat = st.secrets['GIT_PAT']
            repo_name = "https://msquaredds:" + git_pat +\
                        "@github.com/msquaredds/PrivateGitForPublicApp.git"
            Repo.clone_from(repo_name, "./private")
        # Import the private code
        from private import main
        st.markdown(main.private_text)

        # Show the directory
        st.write("Directory /private:")
        st.write(os.listdir(os.path.abspath(os.getcwd()) + '/private'))

        # We can't do the same with a private directory (a directory
        # within a repo), so instead, we'll clone the entire repo and then
        # move the private directory to the top level
        if not os.path.exists('./private_dir') and \
                'private_dir' in os.listdir(os.path.abspath(os.getcwd()) +
                                            '/private'):
            st.write("Copying private_dir to top level...")
            src_path = os.path.abspath(os.getcwd()) + '/private/private_dir'
            tgt_path = os.path.abspath(os.getcwd()) + '/private_dir'
            for src_file in Path(src_path).glob('*.*'):
                st.write(src_file)
                st.write(tgt_path)
                shutil.copy(src_file, tgt_path)

        # Show the directory
        st.write("Directory:")
        st.write(os.listdir(os.path.abspath(os.getcwd())))
        st.write("Directory /private:")
        st.write(os.listdir(os.path.abspath(os.getcwd()) + '/private'))
        st.write("Directory /private_dir:")
        st.write(os.path.exists(os.path.abspath(os.getcwd()) + '/private_dir'))

        tgt_path = os.path.abspath(os.getcwd()) + '/private_dir'
        for tgt_file in Path(tgt_path).glob('*.*'):
            st.write(tgt_file)

        # Import the private code
        import private_dir
        private_dir.test.say_hi()

    else:
        st.write("You don't have the correct password.")



if __name__ == '__main__':
    main()
