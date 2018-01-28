import csv
import os

with open('metadata/UrbanSound8K.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        filename = row["slice_file_name"]
        label = row["class"]

    """
        if not os.path.exists("audio/" + label):
            os.makedirs("audio/" + label)

        if os.path.exists("audio/" + filename):
            os.rename("audio/" + filename, "audio/" + label + "/" + filename)
    """
    
        print(filename, label)