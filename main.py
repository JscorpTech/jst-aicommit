from blackbox import Blackbox
from git import Git
import questionary


class JstAiCommit:

    def __init__(self) -> None:
        ...
    

    def run(self):
        ai = Blackbox()
        git = Git()
        commit = questionary.text("commit: ", default=ai.get_commit(git.diff())).ask()
        git.commit(commit)
        

obj = JstAiCommit()
obj.run()