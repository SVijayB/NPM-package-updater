import urllib.request, json
from pprint import pprint
from test_scripts.send_pr import send_pr
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
            f = open("test\package-lock.json")
            package_lock_data = json.load(f)
            package_lock_data["packages"][""]["dependencies"][dependency] = (
                package_lock_data["packages"][""]["dependencies"][dependency][:1]
                + version
            )
            package_lock_data["packages"][f"node_modules/{dependency}"] = node_modules
            package_lock_data["dependencies"][dependency] = direct_tag
            print(package_lock_data["packages"]["node_modules/axios"])

            # Saving the new package-lock.json
            with open("test\package-lock.json", "w") as outfile:
                json.dump(package_lock_data, outfile, indent=4)
                outfile.write("\n")

            # For package.json file
            f = open("test\package.json")
            package_data = json.load(f)
            try:
                package_data["packages"]["dependencies"][dependency] = (
                    package_data["packages"]["dependencies"][dependency][:1] + version
                )
            except:
                package_data["dependencies"][dependency] = (
                    package_data["dependencies"][dependency][:1] + version
                )
            with open("test\package.json", "w") as outfile:
                json.dump(package_data, outfile, indent=4)
                outfile.write("\n")
            send_pr(json_data[data][1], package_lock_data, package_data)


json_data = {
    "obj_1": [
        "dyte-react-sample-app",
        "https://github.com/dyte-in/react-sample-app",
        "0.24.0",
        "true",
    ],
    "obj_2": [
        "dyte-js-sample-app",
        "https://github.com/dyte-in/javascript-sample-app",
        "0.21.1",
        "false",
    ],
    "obj_3": [
        "dyte-sample-app-backend",
        "https://github.com/dyte-in/backend-sample-app",
        "0.23.0",
        "true",
    ],
}
update_packages(json_data, "axios", "0.23.0")
