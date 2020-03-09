from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time

ch0 = VoltageRatioInput()
ch0.setDeviceSerialNumber(583162)
ch0.setChannel(0)
ch0.openWaitForAttachment(1000)

ch1 = VoltageRatioInput()
ch1.setDeviceSerialNumber(583162)
ch1.setChannel(1)
ch1.openWaitForAttachment(1000)

ch2 = VoltageRatioInput()
ch2.setDeviceSerialNumber(583162)
ch2.setChannel(2)
ch2.openWaitForAttachment(1000)

nick = VoltageRatioInput()
nick.setDeviceSerialNumber(588889)
nick.setChannel(0)
nick.openWaitForAttachment(1000)

excitationvoltage=-10000/0.0459
while True:
    voltageRatio0 = excitationvoltage*ch0.getVoltageRatio() + 1.3 + 2.5
    voltageRatio1 = excitationvoltage*ch1.getVoltageRatio() +1.3
    voltageRatio2 = excitationvoltage*ch2.getVoltageRatio() +1.3
    bucket1 =  voltageRatio0 + voltageRatio1 + voltageRatio2
    nickRatio = excitationvoltage*nick.getVoltageRatio() + 3
    bucket2 = nickRatio
    print(bucket1, bucket 2)

ch0.close()
ch1.close()
ch2.close()
nick.close()
