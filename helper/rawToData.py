import csv

f = open("../results/results9.csv", "r")
fw = open("./finalData.csv", "w")
count = 0


cleaned_data = []
for i in f.readlines():
    if count % 2 == 0:
        ticker = i.split(",", 1)[0]

        raw = i.split(",", 1)[1]
        start = raw.find("<p") + len("<p")
        end = raw.find("</p>")
        substring = raw[start:end]
        final_start = substring.find(">") + len(">")
        final_substring = substring[final_start:]

        cleaned_data.append([ticker, final_substring])

    count += 1

with open("./finalData.csv", 'w', newline='') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=' ')
    for d in cleaned_data:
        datawriter.writerow(d)