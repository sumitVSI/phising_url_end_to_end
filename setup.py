import setuptools

with open("README.md","r",encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "phising_url_end_to_end"
USER_NAME = "sumitVSI"
SRC_REPO = "phising_project"
USER_EMAIL = "sumit.sahoo@voidstarindia.com"


setuptools.setup(

    name = SRC_REPO,
    version = __version__,
    author = USER_NAME,
    author_email = USER_EMAIL,
    description = "VSI phishing url project",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{USER_NAME}/{REPO_NAME}",
    project_urls = {
        'Bug Tracker' : f"https://github.com/{USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)