import extract
import csv
import os


def write_data_set(feature_vector, char):
    feature_vector.append(char)
    with open('datasets.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(feature_vector)
    csvFile.close()


def create_data_set(dir):
    for i in range(97, 123):
        directory = dir + '/' + str(i)
        if not os.listdir(directory):
            continue
        else:
            for filename in os.listdir(directory):
                img_path = directory + '/' + filename
                features = extract.extract(img_path)
                write_data_set(features, i)


if __name__ == '__main__':
    create_data_set('dataset')