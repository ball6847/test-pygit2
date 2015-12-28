Pygit2 using Keypair Credential
===============================

## prerequisite

- libffi-dev (`apt-get install libffi-dev`)
- libgit2-dev (`apt-get install libgit2-dev`)
- python cffi module (`pip install cffi`)

## Install pygit2

```shell
pip install pygit2==0.22.0
```

Note - We need 0.22.0 for now, the latest pygit2 needs libgit2-dev atleast 0.23 which is currently not a default version on ubuntu.

## Example

```python
import pygit2

ssh_user = "git"
ssh_key = {"private": "id_rsa", "public": "id_rsa.pub"}
repo_url = "git@git.bizidea.co.th:Bizidea/Wellman_addon.git"
working_dir = "workdir"

cred = pygit2.Keypair(ssh.user, ssh_key.public, ssh_key.private, "")
repo = pygit2.clone_repository(repo_url, working_dir, bare=False, credentials=cred)
```
