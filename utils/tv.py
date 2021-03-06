channels = {
    "guide": 2.1,
    "gtcn 2.2": 2.2,
    "gtcn 2.3": 2.3,
    "Special Use": 2.4,
    "Special Use 2": 2.5,
    "NASA TV": 2.6,
    "WATL": 3.1,
    "WUPA": 3.2,
    "WSB": 4.1,
    "WCGL": 4.13,
    "Me TV": 4.2,
    "Peachtree TV": 5.13,
    "Fox": 5.3,
    "Movies": 5.4,
    "NBC": 6.1,
    "WGTV": 6.2,
    "NFL": 7.1,
    "MLB": 7.2,
    "NBA": 8.1,
    "CBS Sports": 8.2,
    "NBC Sports": 9.1,
    "Fox Sports South HD": 9.2,
    "Fox Sports South": 9.3,
    "Fox Sports Southeast": 9.4,
    "Fox Sports Southeast HD": 10.1,
    "Fox Sports HD": 10.2,
    "Golf Channel": 11.1,
    "Tennis Channel": 11.2,
    "ESPN": 12.1,
    "ESPN 2": 12.2,
    "ESPNU": 13.1,
    "mtvU": 13.2,
    "MTV": 17.1,
    "VH-1": 17.2,
    "BET": 18.1,
    "CMT": 18.2,
    "HLN": 19.1,
    "CNN": 19.2,
    "Fox News": 20.1,
    "MSNBC": 20.2,
    "CNBC": 21.1,
    "The Weather Channel": 21.2,
    "National Geographic": 22.1,
    "Science Channel": 22.2,
    "Animal Planet": 23.1,
    "History Channel": 23.2,
    "PBS": 24.1,
    "Syfy": 24.2,
    "Discovery Channel": 55.1,
    "Velocity": 55.2,
    "TNT": 56.1,
    "TBS": 56.2,
    "HBO Comedy": 57.1,
    "HBO": 57.2,
    "HBO 2": 58.1,
    "HBO Signature": 58.2,
    "AMC": 59.1,
    "USA": 59.2,
    "BEIN Sports": 65.1,
    "FX": 65.2,
    "FXX": 65.3,
    "IFC": 65.4,
    "Turner Classic": 65.5,
    "Spike": 65.6,
    "American Heroes": 66.1,
    "Travel Channel": 66.2,
    "TLC": 66.3,
    "A&E": 66.4,
    "HGTV": 66.5,
    "Food Network": 66.6,
    "TruTV": 67.1,
    "Comedy Central": 67.2,
    "Bravo": 67.3,
    "Entertainment TV": 67.4,
    "Hallmark Channel": 67.5,
    "Lifetime": 67.6,
    "FYI Network": 68.1,
    "Oprah Winfrey Network": 68.2,
    "Oxygen": 68.3,
    "Game Show Network": 68.4,
    "TV Land": 68.5,
    "Nickelodeon": 68.6,
    "Cartoon Network": 69.1,
    "Freeform": 69.2,
    "Disney Channel": 69.3,
    "C-Span": 69.4,
    "C-Span 2": 69.5,
    "Link TV": 69.6,
    "BBC": 70.1,
    "PTV": 70.2,
    "Sun TV": 70.3,
    "ZEE TV": 70.4,
    "SET": 70.5,
    "B4U Movies": 70.6,
    "TV5 Monde": 71.1,
    "EuroNews": 71.2,
    "My German TV": 71.3,
    "DW-World": 71.4,
    "Willow Cricket": 71.5,
    "Phoenix": 71.6,
    "CCTV": 72.1,
    "Beijing TV": 72.2,
    "TV Japan": 72.3,
    "Univision": 72.4,
    "CNN Español": 72.5,
    "Discovery": 72.6,
    "Tr3s": 72.7,
    "mbc": 72.8,
    "mtv Lebanon": 72.9
}


def find_channel(name):
    chan = 0
    try:
        chan = channels[name]
    except KeyError:
        keys = list(channels.keys())
        keys_lower = [i.lower() for i in keys]
        keys_index = [i.find(name) for i in keys_lower]
        greatest_index = keys_index.index(max(keys_index))
        greatest_name = keys[greatest_index]
        chan = channels[greatest_name]
    return chan


if __name__ == "__main__":
    c = find_channel("mtv")
    print(c)
