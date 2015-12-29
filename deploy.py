from pygit2 import Keypair, Repository, GIT_RESET_HARD, clone_repository
from pprint import pprint
import os

ssh_user = "git"
private_key = "id_rsa"
public_key = "id_rsa.pub"
repo_url = "git@github.com:ritz078/embed.js.git"
working_dir = "workdir"
uid = 1000

# ssh credentials
cred = Keypair("git", public_key, private_key, "")

pid = os.fork()

if pid == 0:
    try:
        os.setgid(uid)
        os.setuid(uid)
        if os.path.isdir(working_dir):
            repo = Repository(os.path.join(working_dir, '.git'))
            # fetch from remote
            remote = repo.remotes[0]
            remote.credentials = cred
            remote.fetch()
            # reset all local change
            head = repo.revparse_single("HEAD")
            repo.reset(head.id, GIT_RESET_HARD)
        else:
            repo = clone_repository(repo_url, working_dir, bare=False, credentials=cred)
    finally:
        os._exit(0)

os.waitpid(pid, 0)
