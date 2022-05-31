from github3 import login, GitHub
import github
import json
import os

# Creating a fork of the repository to the BOT account.
def send_pr(repository, package_lock_data, package_data):

    # Logging in using BOT Creds.
    g = login(token=os.getenv("GH_TOKEN"))
    repository = repository.replace("https://github.com/", "")
    user = repository.split("/")[0]
    repo_name = repository.split("/")[1]

    # Forking the required repository.
    repo = g.repository(user, repo_name)
    repo.create_fork()

    # Updating and commiting data.
    g = github.Github(os.getenv("GH_TOKEN"))
    repo = g.get_repo("PR-Packages-Bot/" + repo_name)

    package_data = json.dumps(package_data, indent=2)
    package_lock_data = json.dumps(package_lock_data, indent=2)

    blob1 = repo.create_git_blob(package_data, "utf-8")
    element1 = github.InputGitTreeElement(
        path="package.json", mode="100644", type="blob", sha=blob1.sha
    )
    blob2 = repo.create_git_blob(package_lock_data, "utf-8")
    element2 = github.InputGitTreeElement(
        path="package-lock.json", mode="100644", type="blob", sha=blob2.sha
    )

    head_sha = repo.get_branch("master").commit.sha

    # Creating a branch
    try:
        branch = repo.create_git_ref(ref=f"refs/heads/update-packages", sha=head_sha)
    except:
        pass
    branch_sha = repo.get_branch("update-packages").commit.sha

    base_tree = repo.get_git_tree(sha=branch_sha)
    tree = repo.create_git_tree([element1, element2], base_tree)
    parent = repo.get_git_commit(sha=branch_sha)
    commit = repo.create_git_commit("Updated packages", tree, [parent])
    branch_refs = repo.get_git_ref("heads/update-packages")
    branch_refs.edit(sha=commit.sha)

    # Creating the PR
    try:
        pr = repo.create_pull(
            title="Updated Packages",
            body="Updated Packages",
            base="master",
            head="update-packages",
        )
    except:
        pr = repo.create_pull(
            title="Updated Packages",
            body="Updated Packages",
            base="main",  # If the default branch name is outdated (Master is the new default)
            head="update-packages",
        )
    return repository + "/pull/" + str(pr.number)
