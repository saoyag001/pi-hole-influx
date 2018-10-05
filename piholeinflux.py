#! /usr/bin/python

from __future__ import print_function
import requests
from time import sleep
from influxdb import InfluxDBClient
from os import path, environ
import traceback
from datetime import datetime
import sys

config = {}

def import_env_vars():
    global config
    config['INFLUX_HOST'] = environ['INFLUX_HOST']
    config['INFLUX_PORT'] = environ['INFLUX_PORT']
    config['INFLUX_USERNAME'] = environ['INFLUX_USERNAME']
    config['INFLUX_PASSWORD'] = environ['INFLUX_PASSWORD']
    config['INFLUX_DATABASE'] = environ['INFLUX_DATABASE']

    config['PIHOLE_API'] = environ['PIHOLE_API']
    config['PIHOLE_INSTANCE_NAME'] = environ['PIHOLE_INSTANCE_NAME']

    config['REPORTING_INTERVAL'] = int(environ['REPORTING_INTERVAL'])

    return config


def send_msg(resp):
    del resp['gravity_last_updated']

    json_body = [
        {
            "measurement": "pihole",
            "tags": {
                "host": config['PIHOLE_INSTANCE_NAME']
            },
            "fields": resp
        }
    ]

    INFLUXDB_CLIENT.write_points(json_body)


if __name__ == '__main__':

    try:
        config = import_env_vars()
    except KeyError as e:
        print("Missing environment variable: %s" % (str(e)))
        sys.exit(1)

    print("Using config: ",config)

    INFLUXDB_CLIENT = InfluxDBClient(config['INFLUX_HOST'],
                                    config['INFLUX_PORT'],
                                    config['INFLUX_USERNAME'],
                                    config['INFLUX_PASSWORD'],
                                    config['INFLUX_DATABASE'])



    while True:
        try:
            api = requests.get(config['PIHOLE_API'])  # URI to pihole server api
            send_msg(api.json())

        except Exception as e:
            msg = 'Failed, to report to InfluxDB:'
            print(msg, str(e))
            print(traceback.format_exc())
            sys.exit(1)

        sleep(config['REPORTING_INTERVAL'])
