from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *

print("testing")
ch1 = VoltageRatioInput()
ch1.setChannel(1)
ch1.openWaitForAttachment(1000)

ch2=VoltageRatioInput()
ch2.setChannel(2)
ch2.openWaitForAttachment(1000)

ch3 = VoltageRatioInput()
ch3.setChannel(0)
ch3.openWaitForAttachment(1000)


excitationvoltage=-10000 / 0.0459


while True:
    voltageRatio1 = excitationvoltage*ch1.getVoltageRatio() +1.3
    voltageRatio2 = excitationvoltage*ch2.getVoltageRatio() +1.3
    voltageRatio3 = excitationvoltage*ch3.getVoltageRatio() +1.3 + 2.5
    bucket1=voltageRatio1+voltageRatio2+voltageRatio3


    print(bucket1)


ch1.close()
ch2.close()
