#!/bin/sh

mosquitto_pub -h 10.123.13.48 \
    -t '/metrotrain/request' \
    -m '{"path":"/tpfunc/metrotrain/power","method":"PUT","headers":[{"request-expired-time":"2021-11-12 11:45:26"},{"request-id":"2"}],"requestBody":{"value":true}}'