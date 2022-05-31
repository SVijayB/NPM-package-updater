from github3 import login, GitHub
import github
import json
import os

# Creating a fork of the repository to the BOT account.
def send_pr(
    repository, package_lock_data, package_data, old_version, new_version, dependency
):

    # Logging in using BOT Creds.
    g = login(token=os.getenv("GH_TOKEN"))
    user_name = g.me().login
    repository = repository.replace("https://github.com/", "")
    original_repo_user = repository.split("/")[0]
    repo_name = repository.split("/")[1]

    # Forking the required repository.
    repo = g.repository(original_repo_user, repo_name)
    repo.create_fork()

    # Updating and commiting data.
    g = github.Github(os.getenv("GH_TOKEN"))
    repo = g.get_repo(f"{user_name}/" + repo_name)

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
    repo = g.get_repo(repository)
    try:
        pr = repo.create_pull(
            title=f"Updated package {dependency} from {old_version} to {new_version}",
            body=f"Updated the version of `{dependency}` from `{old_version}` to `{new_version}`",
            base=f"main",
            head=f"{user_name}:update-packages",
        )
    except:
        pr = repo.create_pull(
            title=f"Updated package {dependency} from {old_version} to {new_version}",
            body=f"Updated the version of `{dependency}` from `{old_version}` to `{new_version}`",
            base=f"master",  # If the default branch name is outdated (P.S: Master is the new default)
            head=f"{user_name}:update-packages",
        )
    return "https://github.com/" + repository + "/pull/" + str(pr.number)
