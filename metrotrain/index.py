#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import json
from thingspro.edge.tag_v1 import tag
from thingspro.edge.http_v1 import http
from thingspro.edge.http_v1.http import http_put


def get_timestamp():
    return int(round(time.time() * 1000000))


@http_put(resource="/metrotrain/power")
def metro_train_power(resource, headers, message):
    global publisher
    try:
        data = dict()
        data['prvdName'] = 'metrotrain'
        data['srcName'] = 'sensor'
        data['tagName'] = 'power'
        data['dataType'] = 'boolean'
        data['dataValue'] = json.loads(message)['value']
        data['ts'] = get_timestamp()
        publisher.publish(data)
    except Exception as e:
        print(e)
    return http.Response(code=200, data="update sensor value")


if __name__ == "__main__":
    # create publisher client instance
    publisher = tag.Publisher()

    # init http function
    metro_train_power()

    # infinite loop
    while True:
        time.sleep(1)
