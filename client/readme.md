# Monitra
## Client

Stores execution details for the latest cron invocation

Information is pulled from 'Pugs', sub-modules that actually fetch the data to be pushed to CloudWatch. 

# Deployment

- Create a ZIP archive of this directory, i.e., client/

- Upload the archive with SCP. Ensure the directory /opt/monitra is already created on the instance, with ownerships with user pi 

	> scp C:\path\to\monitra\client.zip SSH_CONFIG_NAME:/opt/monitra
	
- Extract and setup directory

	> unzip client.zip && mv client/* . && rm -rf client.zip && rm -rf client/

- Update the 'config.py' file with the right values for the environment

- Update configurations within any pugs, if necessary

- Add the following line to crontab -e

    > */15 * * * * cd /opt/monitra/ && /usr/bin/python3 /opt/monitra/monitra.py > /opt/monitra/logs/cmd.log 2>&1

- Ensure permissions exist for the user pi

# Creating Pugs

- Create a file inside the pugs/ directory, i.e., pugs/{PUG_NAME}.py

- Ensure the file implements the methods, main(INSTANCE_NAME)

- The value of the INSTANCE_NAME variable in config.py, will be passed to the pug