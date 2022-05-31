import urllib.request, json
from src.components.send_pr import send_pr
import os

# Method to update the packages if outdated.
def update_packages(json_data, dependency, version):
    for data in json_data:
        # Checking if an update is required.
        if json_data[data][3] == "false":
            # Getting all the information on the new package.
            pkg_url = f"https://registry.npmjs.org/{dependency}/{version}"
            with urllib.request.urlopen(pkg_url) as url:
                pkg_info = json.loads(url.read().decode())

            # For the Node_modules/dependency
            node_modules = {
                "version": pkg_info["version"],
                "resolved": pkg_info["dist"]["tarball"],
                "integrity": pkg_info["dist"]["integrity"],
                "dependencies": pkg_info["dependencies"],
            }
            # For the direct dependency change.
            direct_tag = {
                "version": pkg_info["version"],
                "resolved": pkg_info["dist"]["tarball"],
                "integrity": pkg_info["dist"]["integrity"],
                "requires": pkg_info["dependencies"],
            }

            # For package-lock.json file
            repo_name = json_data[data][1].replace("https://github.com/", "")
            with urllib.request.urlopen(
                "https://raw.githubusercontent.com/"
                + repo_name
                + "/main/package-lock.json"
            ) as url:
                package_lock_data = json.loads(url.read().decode())
            package_lock_data["packages"][""]["dependencies"][dependency] = (
                package_lock_data["packages"][""]["dependencies"][dependency][:1]
                + version
            )
            package_lock_data["packages"][f"node_modules/{dependency}"] = node_modules
            package_lock_data["dependencies"][dependency] = direct_tag

            # For package.json file
            with urllib.request.urlopen(
                "https://raw.githubusercontent.com/" + repo_name + "/main/package.json"
            ) as url:
                package_data = json.loads(url.read().decode())
            try:
                package_data["packages"]["dependencies"][dependency] = (
                    package_data["packages"]["dependencies"][dependency][:1] + version
                )
            except:
                package_data["dependencies"][dependency] = (
                    package_data["dependencies"][dependency][:1] + version
                )
            try:
                pr_link = send_pr(
                    json_data[data][1], (package_lock_data), (package_data)
                )
            except:
                return """ERROR: There seems to be a problem with PR creation. Possible reasons for failure are:<br>
                1. Your GitHub token was not provided.<br>
                2. You are not connected to the internet.<br>
                3. Repository links provided are broken.<br>
                4. PR already exists.<br>
                
                Please look into the above mentioned errors and try again.
            """
            json_data[data].append(pr_link)
        else:
            json_data[data].append("No update required")
    return json_data
