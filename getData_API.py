from urllib.request import urlopen , Request
import csv
import json

def get_jsonparsed_data(my_url):


    req = Request(url=my_url, headers=headers)


    response = urlopen(req)
    data = response.read().decode("utf-8")
    return json.loads(data)

filename = "sneakerData.csv"
f = open(filename,"w+")
headers = "brand,colorway,gender,name,title,releaseDate,retailPrice,belowRetail,shoe,missingData\n"
f.write(headers)

groups = list(headers.split(","))
groups = [x.strip(' ') for x in groups]
del groups[-1]


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

url = ("https://stockx.com/api/browse?page=1&productCategory=sneakers")
parsed_data = get_jsonparsed_data(url)
page_data = parsed_data['Pagination']

foo = 0
print("Collecting Data")
for x in range(int(page_data['limit'])):
    url = ("https://stockx.com/api/browse?page="+str(x)+"&productCategory=sneakers")

    parsed_data = get_jsonparsed_data(url)

    products = parsed_data['Products']
    for p in products:
        toWrite = ""
        missingData = False
        for g in groups:
            try:
                f.write(str(p[g])+",")
            except TypeError:
                f.write("N/A,")
                missingData = True
        if missingData:
            f.write("True\n")
            foo += 1
            print("error"+str(foo))
        else:
            f.write("False\n")
print("Data Collection Complete. "+str(foo)+" NoneType Entries. See sneakerData.csv")
    #print(page_data['limit'])


'''
Utilize --market-- object identifier for price stuff
'''
