def get_file_path(message, ext="wpl"):
    """
    Get playlist file path
    """
    while True:
        response = input(message).strip('"')
        if response[-3:] in ext:
            return response


def main():
    """
    Conver wpl or zpl playlist files to M3U
    """

    wpl_path = get_file_path("WPL/ZPL playlist file path?\n\t", ["wpl", "zpl"])
    wpl = open(wpl_path, "r")
    m3u = open(wpl_path[:-4] + "-3MU.m3u", "w+")

    m3u.write("#EXTM3U\n")
    lines = wpl.read().splitlines()
    for line in lines:
        if "<media src=" in line:
            song = line.split('"')[1].replace("\\", '/')
            m3u.write(song + "\n")
    
    wpl.close() 
    m3u.close()

if __name__ == "__main__":
    main()