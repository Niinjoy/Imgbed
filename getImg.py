import urllib.request, csv

ganpll = csv.reader(open('GANPLL.csv', newline=''))
for row in ganpll:
	urllib.request.urlretrieve("http://cube.rider.biz/visualcube.php?fmt=svg&view=plan&case="+row[1], "cubeImg/"+row[0]+".svg")

# urllib.request.urlretrieve("http://cube.rider.biz/visualcube.php?fmt=svg&case=URU'R'&stage=f2l&bg=t&view=trans&cc=grey&co=40", "cubeImg/test2.svg")
# urllib.request.urlretrieve("http://cube.rider.biz/visualcube.php?fmt=svg&view=plan&case=", "cubeImg/test2.svg")