import urllib.request, json
import os

# Method to update the packages if outdated.
def update_packages(json_data, dependency, version):
    for data in json_data:
        print(data)
