import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


def lookfor(item):
    open_tr = html.find('<tr>', i)
    close_tr = html.find("</tr>", open_tr)  
    newstring = html[open_tr:close_tr]
    start = newstring.find(item)
    end = newstring.find('</', start)
    newval = (newstring[start+len(item):end])

    if "title" in item:
        start = (newval.find('/">'))
        newval = newval[start+3:]

    if "artist" in item:
        start = (newval.find('/">'))
        newval = newval[start+3:]

    return newval, close_tr



def all_val():
    position, close_tr = find('"position">')
    title, close_tr = find('class="title">')
    artist, close_tr = find('class="artist')

    return position, title, artist, close_tr


    
if __name__ == "__main__":
    list = []
    i = 0
    loop = 0
    html = scrape(url)
    while loop < 10:
        position, title, artist, close_tr = find_all_values()
        print(position)
        eachrank = ([position, title, artist])
        list.append(eachrank)
        i = close_tr
        loop = loop + 1
    print(f"{'Position:-':20}{'Name:-':30}{'Artist:-':30}")
    print("")

    for loop in list:
        print(f'{loop[0]:5}{loop[1]:^30}{loop[2]:>30}')
