import urllib.request, json
import os

# Method to update the packages if outdated.
def update_packages(json_data, dependency, version):
    for data in json_data:
        # Checking if an update is required.
        if json_data[data][3] == "false":
            # Getting all the information on the new package.
            pkj_url = f"https://registry.npmjs.org/{dependency}/{version}"
            with urllib.request.urlopen(pkj_url) as url:
                pkj_info = json.loads(url.read().decode())

            # For the Node_modules/dependency
            node_modules = {
                "new_version": pkj_info["version"],
                "resolved": pkj_info["dist"]["tarball"],
                "integrity": pkj_info["dist"]["integrity"],
                "dependencies": pkj_info["dependencies"],
            }
            # For the direct dependency change.
            direct_tag = {
                "new_version": pkj_info["version"],
                "resolved": pkj_info["dist"]["tarball"],
                "integrity": pkj_info["dist"]["integrity"],
                "requires": pkj_info["dependencies"],
            }
            f = open("test\package-lock.json")
            data = json.load(f)
            print(data)


json_data = {
    "obj_1": [
        "dyte-react-sample-app",
        "https://github.com/dyte-in/react-sample-app/",
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
