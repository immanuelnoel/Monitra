import os
import datetime

primary_path = '/media/exthd/cctv/xiaomi_camera_videos/'
camera_list = [{'id': 'fsdgfgfdsg', 'name': 'cctv_parking'}, {'id': 'adfdsfsdcv', 'name': 'cctv_maindoor'}]

def main(INSTANCE_NAME):

    values = []
    for camera in camera_list:

        # Get latest directory
        camera_path = primary_path + camera['id']
        directoryList = os.listdir(camera_path)
        latest_directory = max([os.path.join(camera_path, basename) for basename in directoryList], key=os.path.getctime)

        nameparts = latest_directory.split('/')
        timepart = nameparts[len(nameparts)-1]
        year = int(timepart[0:4])
        month = int(timepart[4:6])
        date = int(timepart[6:8])
        hour = int(timepart[8:])

        latest_directory_file_count = len([name for name in os.listdir(latest_directory)])

        latest_directory_date = datetime.datetime(year, month, date, hour, latest_directory_file_count)

        current_date = datetime.datetime.now()
        difference_in_seconds = (current_date - latest_directory_date).total_seconds()

        values.append({"device": camera['name'], "metric": "last_recording", "value": difference_in_seconds})

    return values