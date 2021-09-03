from random import shuffle
#import pandas as pd
from csv import reader

def getDistance(test, train):
    test = test[:len(test)-1]
    distance = []

    for training in train:
        x = 0.0
        for i in range(9): #str values
            if test[i] == training[i]:
                x += 0.0
            else:
                x += 1.0

        for i in range(9, 13):
            x += (float(test[i]) - float(training[i])) ** 2
        
        
        for i in range(13, 16):
            if test[i] == training[i]:
                x += 0.0
            else:
                x += 1.0

        distance.append([x ** .5, training[-1]])

    return distance


def getPrediction(distance, k):
    output_values = [dist[-1] for dist in distance[:k]]
    prediction = max(set(output_values), key=output_values.count)
    return prediction


def evaluateAlgorithm(train, test, k, oFile):
    #distance = []
    count = 0
    for i in range(len(test)):
        test_values = test[i]
        distance = getDistance(test_values, train)
        distance.sort()

        prediction = getPrediction(distance, k)
        #oFile.write([str(x) + ',' for x in test_values] + ',' + prediction + '\n')
        List = [test_values, prediction]
        for list in List:
            oFile.write(str(list) + ',')

        oFile.write('\n')

        if prediction == test_values[-1]:
            count += 1

    oFile.write('accuracy : ' + str(count / len(test)) + '\n\n')
    return count / len(test)


def testUserInput(train, test, k):
    
    distance = getDistance(test, train)
    distance.sort()

    prediction = getPrediction(distance, k)
    
    return prediction


if __name__ == '__main__':
    fileName = 'xAPI-Edu-Data.csv'
    oFile = open('out.txt', 'w')
    

     
    file = open(fileName, 'r')
    
    
    data = []
    csv_reader = reader(file)
    header = next(csv_reader)
    
    count = 0
    for row in csv_reader:
        data += [row]
        count += 1
    
    
    shuffle(data)
    shuffledData = list.copy(data)
    
    
    numberOfFold = int(input("number of fold: "))
    k = int(input('value of k: '))
    percent = int(len(shuffledData) / numberOfFold)
    accuracy = []
    
    for i in range(numberOfFold):
        start = i * numberOfFold
        end = start + percent
        test = shuffledData[start : end]
        train = shuffledData[: start] + shuffledData[end-1:]
        
        accuracy.append(evaluateAlgorithm(train, test, k, oFile))
        
    
    print(accuracy)
    meanAccuracy = sum(accuracy) / len(accuracy)
    print('mean accuracy : ', meanAccuracy)

    file.close()
    oFile.close()
    
    #consider it as user input 
    #predict a student
    
    input1 = ['M', 'KW', 'KuwaIT', 'lowerlevel', 'G-02', 'A', 
                'Math', 'S', 'Father', '60', '84', '2', '8', 'Yes', 'Good', 'Under-7', '']

    result = testUserInput(shuffledData, input1, k)
    print('predicted result: ', result)
    
    