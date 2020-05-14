import time
from git import Repo


def git_push(file_list, commit_message):
    repo = Repo('.')
    for file in file_list:
        repo.index.add(file)
    repo.index.commit(commit_message)
    origin = repo.remotes.origin
    try:
        origin.pull()
        origin.push()
    except Exception as error:
        print(error)
        time.sleep(300)
        git_push(file_list, commit_message)


git_push(['test.txt'], 'hello world commit')

