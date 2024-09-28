entries = [
    {
        "NAME": "FURBALL",
        "TYPE": "ARCTIC",
        "DESC": "The ordinary FURBALL is a penguin-duck combination, with a slight hint of cat. A real menace."
    },
    {
        "NAME": "DRUG DEALER FURBALL",
        "TYPE": "CITY",
        "DESC": "This noble FURBALL sells drugs in MERCURY DRUGSTORE to earn a living and support his children."
    },
    {
        "NAME": "BRAINIAC FURBALL",
        "TYPE": "CITY",
        "DESC": "Dangerously smart crazy scientist FURBALL that has experimented on his own body."
    },
    {
        "NAME": "RICH FURBALL",
        "TYPE": "CITY",
        "DESC": "FURBALLs which have made it big in the business world through fair means or foul."
    },
    {
        "NAME": "BEDTIME FURBALL",
        "TYPE": "CITY",
        "DESC": "Sleeps in the light, lives in the night, BEDTIME FURBALLs keep the world working right."
    },
    {
        "NAME": "BEE FURBALL",
        "TYPE": "FOREST",
        "DESC": "BEE FURBALLs cannot talk; instead, they use flying dances to communicate with each other."
    },
    {
        "NAME": "APPLE FURBALL",
        "TYPE": "FOREST",
        "DESC": "Falling from trees like raindrops from cloud, APPLE FURBALLs defend the FOREST from worms."
    },
    {
        "NAME": "WAR FURBALL",
        "TYPE": "FRONTIER",
        "DESC": "Experienced war veterans; WAR FURBALLs actually despise war, and would never want another."
    },
    {
        "NAME": "ANGEL FURBALL",
        "TYPE": "MYTHICAL",
        "DESC": "Goody-two-shoes FURBALLs that always seems to say what he thinks is right."
    },
    {
        "NAME": "DEVIL FURBALL",
        "TYPE": "MYTHICAL",
        "DESC": "Baddy-two-shoes FURBALLs that always seems to say what he thinks is wrong."
    },
    {
        "NAME": "JUDGE FURBALL",
        "TYPE": "MYTHICAL",
        "DESC": "The father of ANGEL and DEVIL FURBALLs casts judgements in criminal trials." 
    },
    {
        "NAME": "DIRTBALL",
        "TYPE": "FRONTIER",
        "DESC": "These smaller-than-usual FURBALLs plan ambushes from dirt holes at the FUR-TANOOK FRONTIER."
    }
]

import json

BEGIN = """
<!DOCTYPE html>
<head>
    <title>The Furball Dex</title>
    <link rel="stylesheet" href="default.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>THE FURBALL DEX 2</h1>
    <table>
"""
END = """    </table>
</body>
"""
TEMPLATE = """
        <tr>
            <td>
                <img src="<%IMAGE%>" class="furball">
            </td>
            <td>
                <span class="number"><%NUMBER%></span>
                <span class="name"><%NAME%></span>
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
    for i, entry in enumerate(entries, start=1):
        furball_data = TEMPLATE
        entry.update(
            {"NUMBER": str(i).zfill(3), "IMAGE": "furballs/" + entry["NAME"] + ".png"}
        )
        for key, value in entry.items():
            furball_data = furball_data.replace(f"<%{key}%>", str(value))
        out += furball_data
    out += END
    print(out)


if __name__ == "__main__":
    main()
