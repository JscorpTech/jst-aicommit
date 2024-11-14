from blackbox import Blackbox
from git import Git
import questionary
from rich import print


class JstAiCommit:

    def __init__(self) -> None:
        ...
    

    def run(self):
        ai = Blackbox()
        git = Git()
        status, changes = git.diff()
        if not status or len(changes.strip()) == 0:
            print("[red bold] No changes to commit.[/red bold]")
            exit()
        commit = questionary.text("commit: ", default=ai.get_commit()).ask()
        git.commit(commit)
        

obj = JstAiCommit()
obj.run()