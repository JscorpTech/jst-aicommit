import subprocess


class Git:

    def __init__(self) -> None:
        ...
    
    def get_stash(self):
        try:
            output = subprocess.run(["git","stash"], capture_output=True, text=True, check=True)
            print(output.stdout)
        except Exception as e:
            print(e.stderr.strip())


obj = Git()
obj.get_stash()