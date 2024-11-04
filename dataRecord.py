# what am I trying to do here
# set all torques to zero so that the exoskeleton is completely passive
# record odrive loop
# record imu data
# put timestamed data into csv, timestamp is importatn since IMU will not run at same rate as odriveloop
# hi there I'm Marcus :D this is to collect data on gaits so that people can make a neural network for next move prediction, ground contact sensors may help in the future (possible future checkhov's gun?)

#odrive0 (left hip ad/abduction) odrive1 (left hip elevation), odrive2 (Knee), odrive3 (left left ankle), odrive4(left right ankle), odrive5 (right hip ad/abduction) odrive6 (right hip elevation), odrive7 (Right Knee), odrive8 (right left ankle), odrive8 (right right ankle)
#(odrive0, odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9)

import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import time

current_limit = 35.0
velocity_limit = 40 #rev/s but since unpowered it is just so it doesn't estop lock


# This async function will constantly get postion data from the socket.
async def noTorque(odrive0, odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9):
    for odrive in (odrive0, odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9):
        odrive.set_torque(0)






async def main():

    #Left Leg
    odrive0 = pyodrivecan.ODriveCAN(0)
    odrive0.initCanBus()

    
    odrive1 = pyodrivecan.ODriveCAN(1)
    odrive1.initCanBus()

    
    odrive2 = pyodrivecan.ODriveCAN(2)
    odrive2.initCanBus()

    
    odrive3 = pyodrivecan.ODriveCAN(3)
    odrive3.initCanBus()
    
    odrive4 = pyodrivecan.ODriveCAN(4)
    odrive4.initCanBus()

    #Right Leg
    odrive5 = pyodrivecan.ODriveCAN(5)
    odrive5.initCanBus()

    odrive6 = pyodrivecan.ODriveCAN(6)
    odrive6.initCanBus()

    odrive7 = pyodrivecan.ODriveCAN(7)
    odrive7.initCanBus()

    odrive8 = pyodrivecan.ODriveCAN(8)
    odrive8.initCanBus()
    
    odrive9 = pyodrivecan.ODriveCAN(9)
    odrive9.initCanBus()

    
    # Configure each ODrive
    for odrive in (odrive0, odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9):
        odrive.set_limits(velocity_limit=velocity_limit, current_limit=current_limit)
        await asyncio.sleep(0.2)
        odrive.clear_errors(identify=False)
        await asyncio.sleep(0.2)
        odrive.set_controller_mode("torque_control")
        await asyncio.sleep(0.2)  # Delay to prevent command overlap on CAN bus
    await asyncio.sleep(1)
    print("all set! torque control at 0 nm set")

   

    while True:
        try:
            odrive0.loop(),
            odrive1.loop(),
            odrive2.loop(),
            odrive3.loop(),
            odrive4.loop(),
            odrive5.loop(),
            odrive6.loop(),
            odrive7.loop(),
            odrive8.loop(),
            odrive9.loop(),
            noTorque(odrive0,  odrive1, odrive2, odrive3, odrive4),

        except KeyboardInterrupt:
            break    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated with keyboard interrupt.")



