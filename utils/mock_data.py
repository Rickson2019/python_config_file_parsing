# https://github.com/aws-samples/sbs-iot-data-generator/blob/master/sbs.py

# generate Temperature values
def getTemperatureValues():
    data = {}
    data['value'] = random.randint(15, 35)
    data['deviceParameter'] = 'Temperature'
    data['deviceId'] = random.choice(deviceNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# generate Humidity values
def getHumidityValues():
    data = {}
    data['value'] = random.randint(50, 90)
    data['deviceParameter'] = 'Humidity'
    data['deviceId'] = random.choice(deviceNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

# generate Sound values
def getSoundValues():
    data = {}
    data['deviceValue'] = random.randint(100, 140)
    data['deviceParameter'] = 'Sound'
    data['deviceId'] = random.choice(deviceNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data