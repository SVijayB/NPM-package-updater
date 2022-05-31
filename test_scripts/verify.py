import csv
import pprint
import urllib.request, json


def verify(file_location, dependency, version):
    # Converting CSV file to JSON Data for easier access.
    json_data = {}
    with open(file_location, "r") as file:
        csvreader = csv.reader(file)
        next(file)
        i = 1
        for rows in csvreader:
            json_data[f"obj_{i}"] = [rows[0], rows[1]]
            i += 1
    # Obtain the version of the dependency from the Package.json file and adding it to JSON data.
    for obj in json_data:
        repo_url = json_data[obj][1].replace("https://github.com/", "")
        pkj_url = f"https://raw.githubusercontent.com/{repo_url}/master/package.json"
        with urllib.request.urlopen(pkj_url) as url:
            data = json.loads(url.read().decode())
            try:
                all_dependencies = data["packages"]["dependencies"]
            except:
                all_dependencies = data["dependencies"]
        if dependency in all_dependencies:
            json_data[obj].append(all_dependencies[dependency].replace("^", ""))
            if json_data[obj][2] >= version:
                json_data[obj].append("true")
            else:
                json_data[obj].append("false")
        else:
            json_data[obj].append("NULL", "false")

    pprint.pprint(json_data)
    print(view_builder(json_data))


def view_builder(json_data):
    table_data = ""
    for row in json_data:
        table_data = (
            table_data
            + f"""
                        <tr>
                            <td> {json_data[row][0]} </td>
                            <td> {json_data[row][1]} </td>
                            <td> {json_data[row][3]} </td>
                            <td> {json_data[row][2]} </td>
                        </tr>"""
        )
    view = f"""
        <html>
            <head><title> Result from Query </title></head>
            <body>
                <h2> Result from Query </h2>
                <table>
                    <thead>
                        <tr>
                            <th> Name </th>
                            <th> Repo </th>
                            <th> Version </th>
                            <th> Version_Satisfied </th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_data}
                    </tbody>
                </table>
            </body>
        """
    return view


verify("example/verify_file.csv", "axios", "0.23.0")
