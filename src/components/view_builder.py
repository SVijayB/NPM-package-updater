def view_builder(json_data, update):
    table_data = ""

    # Changing view as per the update status.
    if update == True:
        for row in json_data:
            table_data = (
                table_data
                + f"""
                            <tr>
                                <td> {json_data[row][0]} </td>
                                <td> {json_data[row][1]} </td>
                                <td> {json_data[row][2]} </td>
                                <td> {json_data[row][3]} </td>
                                <td> {json_data[row][4]} </td>
                            </tr>"""
            )
    else:
        for row in json_data:
            table_data = (
                table_data
                + f"""
                            <tr>
                                <td> {json_data[row][0]} </td>
                                <td> {json_data[row][1]} </td>
                                <td> {json_data[row][2]} </td>
                                <td> {json_data[row][3]} </td>
                            </tr>"""
            )

    # Final HTML Table rendering.
    view = f"""
        <html>
            <head>
                <title> Result from Query </title>
                <style>
                table, th, td \u007b
                    border: 1px solid black;
                    \u007d
                </style>
            </head>
            <body>
                <h2> Result from Query </h2>
                <table style="width:100%">
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
