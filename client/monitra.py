import os
import sys
import json
import requests
import importlib

import config

def main():

    payload_data = []

    pug_list = [name for name in os.listdir("pugs") if name != "__pycache__"]
    for pug in pug_list:

        try:
            pug_name = pug.split('.')[0]
            module = importlib.import_module('.' + pug_name, package='pugs')
            pug_method = getattr(module, "main")
            pug_data = pug_method(config.INSTANCE_NAME)

            print("Pug, " + pug_name)
            for data in pug_data:

                print(str(data['metric']) + " for " + str(data['device']) + ": " + str(data['value']))
                payload_data.append(data)

            print("========================")

        except:
            e = sys.exc_info()[0]
            print("Pug " + pug_name + " failed with, " + str(e))

    http_status = send_data(payload_data)
    print(http_status.content.decode())


def send_data(payload):

    http_status = requests.put(config.AWS_API_Endpoint,
            data=json.dumps(payload),
            headers={'content-type':'text/plain', 'api-key':config.AWS_API_Key})
    return http_status


if __name__ == "__main__":
    main()