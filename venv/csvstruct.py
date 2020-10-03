import csv

with open('twitter.csv', 'w', newline='') as csvfile:
    fieldnames = ['id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
#just to create a csv file with file name twitter.csv to save ids from hashtagstream.py

#follow me on instagaram to get your doubts cleared 
#instagram:- lzy_geek