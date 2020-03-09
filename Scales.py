from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time

w1ch0 = VoltageRatioInput()
w1ch0.setDeviceSerialNumber(583162)
w1ch0.setChannel(0)
w1ch0.openWaitForAttachment(1000)

w1ch1 = VoltageRatioInput()
w1ch1.setDeviceSerialNumber(583162)
w1ch1.setChannel(1)
w1ch1.openWaitForAttachment(1000)

w1ch2 = VoltageRatioInput()
w1ch2.setDeviceSerialNumber(583162)
w1ch2.setChannel(2)
w1ch2.openWaitForAttachment(1000)

w2ch0 = VoltageRatioInput()
w2ch0.setDeviceSerialNumber(588889)
w2ch0.setChannel(0)
w2ch0.openWaitForAttachment(1000)

w2ch1 = VoltageRatioInput()
w2ch1.setDeviceSerialNumber(588889)
w2ch1.setChannel(1)
w2ch1.openWaitForAttachment(1000)

w2ch2 = VoltageRatioInput()
w2ch2.setDeviceSerialNumber(588889)
w2ch2.setChannel(2)
w2ch2.openWaitForAttachment(1000)

w3ch0 = VoltageRatioInput()
w3ch0.setDeviceSerialNumber(______)
w3ch0.setChannel(0)
w3ch0.openWaitForAttachment(1000)

w3ch1 = VoltageRatioInput()
w3ch1.setDeviceSerialNumber(______)
w3ch1.setChannel(1)
w3ch1.openWaitForAttachment(1000)

w3ch2 = VoltageRatioInput()
w3ch2.setDeviceSerialNumber(______)
w3ch2.setChannel(2)
w3ch2.openWaitForAttachment(1000)

w4ch0 = VoltageRatioInput()
w4ch0.setDeviceSerialNumber(______)
w4ch0.setChannel(0)
w4ch0.openWaitForAttachment(1000)

w4ch1 = VoltageRatioInput()
w4ch1.setDeviceSerialNumber(______)
w4ch1.setChannel(1)
w4ch1.openWaitForAttachment(1000)

w4ch2 = VoltageRatioInput()
w4ch2.setDeviceSerialNumber(______)
w4ch2.setChannel(2)
w4ch2.openWaitForAttachment(1000)

w5ch0 = VoltageRatioInput()
w5ch0.setDeviceSerialNumber(______)
w5ch0.setChannel(0)
w5ch0.openWaitForAttachment(1000)

w5ch1 = VoltageRatioInput()
w5ch1.setDeviceSerialNumber(______)
w5ch1.setChannel(1)
w5ch1.openWaitForAttachment(1000)

w5ch2 = VoltageRatioInput()
w5ch2.setDeviceSerialNumber(______)
w5ch2.setChannel(2)
w5ch2.openWaitForAttachment(1000)


excitationvoltage=-10000/0.0459

while True:
    w1ch0weight = excitationvoltage*w1ch0.getVoltageRatio() + 1.3 + 2.5
    w1ch1weight = excitationvoltage*w1ch1.getVoltageRatio() +1.3
    w1ch2weight = excitationvoltage*w1ch2.getVoltageRatio() +1.3
    bucket1 =  w1ch0weight + w1ch1weight + w1ch2weight

    w2ch0weight = excitationvoltage*w2ch0.getVoltageRatio() + 3
    w2ch1weight = excitationvoltage*w2ch1.getVoltageRatio() + 3
    w2ch2weight = excitationvoltage*w2ch2.getVoltageRatio() + 3
    bucket2 = w2ch0weight + w2ch1weight + w2ch2weight

    w3ch0weight = excitationvoltage*w3ch0.getVoltageRatio() + 1.3
    w3ch1weight = excitationvoltage*w3ch1.getVoltageRatio() +1.3
    w3ch2weight = excitationvoltage*w3ch2.getVoltageRatio() +1.3
    bucket3 =  w3ch0weight + w3ch1weight + w3ch2weight

    w4ch0weight = excitationvoltage*w4ch0.getVoltageRatio() + 1.3
    w4ch1weight = excitationvoltage*w4ch1.getVoltageRatio() +1.3
    w4ch2weight = excitationvoltage*w4ch2.getVoltageRatio() +1.3
    bucket4 =  w4ch0weight + w4ch1weight + w4ch2weight

    w5ch0weight = excitationvoltage*w5ch0.getVoltageRatio() + 1.3
    w5ch1weight = excitationvoltage*w5ch1.getVoltageRatio() +1.3
    w5ch2weight = excitationvoltage*w5ch2.getVoltageRatio() +1.3
    bucket5 =  w5ch0weight + w5ch1weight + w5ch2weight



    print(bucket1, bucket2, bucket3, bucket4, bucket5)

w1ch0.close()
w1ch1.close()
w1ch2.close()
w2ch0.close()
w2ch1.close()
w2ch2.close()
w3ch0.close()
w3ch1.close()
w3ch2.close()
w4ch0.close()
w4ch1.close()
w4ch2.close()
w5ch0.close()
w5ch1.close()
w5ch2.close()
