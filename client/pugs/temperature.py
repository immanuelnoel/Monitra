from subprocess import PIPE, Popen

def main(INSTANCE_NAME):

    metricname = "measure_temp"
    metricparam = ""

    process = Popen(['vcgencmd', metricname, metricparam], stdout=PIPE)
    output, _error = process.communicate()

    temp = output.decode().split("=")[1].split("'")[0]

    returnValue = []
    returnValue.append({"device": INSTANCE_NAME, "metric": "temperature", "value": temp})

    return returnValue