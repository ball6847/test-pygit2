import pygit2
from pprint import pprint
from os import path

ssh_user = "git"
ssh_key = {
    'private': "id_rsa",
    'public': "id_rsa.pub"
}
repo_url = "git@git.bizidea.co.th:Bizidea/Wellman_addon.git"
working_dir = "workdir"

# ssh credentials
cred = pygit2.Keypair(ssh_user, ssh_key['public'], ssh_key['private'], "")
callback = pygit2.RemoteCallbacks(credentials=cred)

if path.isdir(working_dir):
    repo = pygit2.Repository(path.join(working_dir, '.git'))
    # use first remote by default
    remote = repo.remotes[0]
    # remote.fetch(credentials=cred)
else:
    repo = pygit2.clone_repository(repo_url, working_dir, bare=False, credentials=cred)
