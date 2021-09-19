import logging

import boto3
from chalice import Chalice, Rate

app = Chalice(app_name='schedule-lambda')
app.log.setLevel(logging.INFO)

ec2 = boto3.client('ec2')


@app.schedule(Rate(1, unit=Rate.MINUTES))
def regions(event):
    response = ec2.describe_regions()
    app.log.info(response['Regions'])
