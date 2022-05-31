from github3 import login, GitHub
import github
import os


def gh_api_test():
    g = login(token=os.getenv("GH_TOKEN"))
    user_name = g.me()
    user_name = user_name.login
    repository = "https://github.com/dyte-in/javascript-sample-app"
    repository = repository.replace("https://github.com/", "")
    original_repo_user = repository.split("/")[0]
    dependency = "axios"
    old_version = "0.21.1"
    new_version = "0.23.0"
    repo_name = repository.split("/")[1]
    print(repository)
    print(user_name + "/" + repository.split("/")[1])
    g = github.Github(os.getenv("GH_TOKEN"))
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
    print(pr)


gh_api_test()
