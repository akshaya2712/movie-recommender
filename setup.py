from setuptools import setup
with open("README.md","r",encoding="utf-8") as fh:
    long_description=f.read()
    
AUTHOR_NAME='GayatriAkshaya'
SRC_REPO='src'
LIST_REQUIREMENTS=['streamlit']
setup(
      name=SRC_REPO,
      version='0.0.1',
      author=AUTHOR_NAME,
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      author_email='akshayavobbilisetti@gmail.com',
      long_description=long_description,
      long_description_content_type='text/markdown',
      package=[SRC_REPO],
      install_requires= LIST_REQUIREMENTS
      )
