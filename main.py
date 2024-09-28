import json

BEGIN = """
<!DOCTYPE html>
<head>
    <title>The Furball Dex</title>
    <link rel="stylesheet" href="default.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <audio autoplay loop src="pallet.mp3"></audio>
    <h1>THE FURBALL DEX 2</h1>
    <table>
        <tbody>
"""
END = """   </tbody>
    </table>
</body>
"""
TEMPLATE = """
        <tr>
            <td>
                <img src="<%IMAGE%>" class="furball">
            </td>
            <td>
                <span class="number">No.<%NUMBER%></span>
                <span class="name"><%NAME%></span>
                <span class="name"><%TYPE%> TYPE</span>
            </td>
        </tr>
        <tr>
            <td colspan=2>
                <span class="desc">
                    <%DESC%>
                </span>
            </td>
        </tr>
"""


def main():
    out = BEGIN
    with open("data.json", "r") as f:
        data = json.loads(f.read())
    for i, entry in enumerate(data, start=1):
        furball_data = TEMPLATE
        entry.update(
            {"NUMBER": str(i).zfill(3), "IMAGE": "furballs/" + entry["NAME"] + ".png"}
        )
        for key, value in entry.items():
            furball_data = furball_data.replace(f"<%{key}%>", str(value))
        out += furball_data
    out += END
    with open("index.html", "w") as f:
        f.write(out)


if __name__ == "__main__":
    main()
