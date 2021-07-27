import logging

from opcua import Client
from opcua import ua

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARN)

    client = Client("opc.tcp://10.123.13.13:4840")
    client.set_user("moxa")
    client.set_password("moxamoxa")
    try:
        client.connect()
        client.load_type_definitions()

        current = client.get_node("ns=2;s=metrotrain.sensor.current")
        datavalue = ua.DataValue(ua.Variant(1.234, ua.VariantType.Double))
        current.set_value(datavalue)

        voltage = client.get_node("ns=2;s=metrotrain.sensor.voltage")
        datavalue = ua.DataValue(ua.Variant(3.1415, ua.VariantType.Double))
        voltage.set_value(datavalue)
    except Exception as e:
        print(e)
    finally:
        client.disconnect()