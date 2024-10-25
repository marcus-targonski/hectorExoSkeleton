import socket
import pyodrivecan
import asyncio
from datetime import datetime, timedelta
import time


# This async function will constantly get postion data from the socket.
async def moveLegs(odrive0,  odrive1, odrive2, odrive3, odrive4):
    while True:
            odrive0.set_position(0)
            odrive2.set_position(-6.5) #knee
            odrive1.set_position(6.5) #hip elevator
            odrive3.set_position(0)
            odrive4.set_position(0)

current_limit = 35.0
velocity_limit = 2.0



async def main():
    

    odrive0 = pyodrivecan.ODriveCAN(0)
    odrive0.initCanBus()

    #LEG 1
    #node 2 front left hipx
    odrive1 = pyodrivecan.ODriveCAN(1)
    odrive1.initCanBus()

    # Set up Node 1 front left shoulder (y)
    odrive2 = pyodrivecan.ODriveCAN(2)
    odrive2.initCanBus()
    #odrive1.setAxisState("closed_loop_control")

    # Set up Node_ID 0 front left knee
    odrive3 = pyodrivecan.ODriveCAN(3)
    odrive3.initCanBus()
    
    odrive4 = pyodrivecan.ODriveCAN(4)
    odrive4.initCanBus()

    
    # Configure each ODrive
    for odrive in (odrive0,  odrive1, odrive2, odrive3, odrive4):
        odrive.set_limits(velocity_limit=velocity_limit, current_limit=current_limit)
        time.sleep(0.2)
        odrive.clear_errors(identify=False)
        await asyncio.sleep(0.2)
        odrive.set_controller_mode(control_mode_name="position_control", input_mode_name="pos_filter")
        await asyncio.sleep(0.2)  # Delay to prevent command overlap on CAN bus
    
    #Leg1
        odrive0.set_position(0)
        odrive2.set_position(-6.5) #knee
        odrive1.set_position(6.5) #hip elevator
        odrive3.set_position(0)
        odrive4.set_position(0)

    await asyncio.sleep(2)

   

    while True:
        try:
           
            #Leg1
            odrive0.loop(),
            odrive1.loop(),
            odrive2.loop(),
            odrive3.loop(),
            odrive4.loop(),
            moveLegs(odrive0,  odrive1, odrive2, odrive3, odrive4),

        except KeyboardInterrupt:
            break    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated with keyboard interrupt.")