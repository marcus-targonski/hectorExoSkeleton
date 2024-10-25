import time
import pyodrivecan
import asyncio

current_limit = 35.0
velocity_limit = 4.0
counter = 0

#odrive0 (left hip ad/abduction) odrive1 (left hip elevation), odrive2 (Knee), odrive3 (left left ankle), odrive4(left right ankle), odrive5 (right hip ad/abduction) odrive6 (right hip elevation), odrive7 (Right Knee), odrive8 (right left ankle), odrive8 (right right ankle)

async def calibrate(odrive0, odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9):
    #Left
    odrive0.set_absolute_position(0)
    odrive1.set_absolute_position(0)
    odrive2.set_absolute_position(0)
    odrive3.set_absolute_position(0)
    odrive4.set_absolute_position(0)

    #Right
    odrive5.set_absolute_position(0)
    odrive6.set_absolute_position(0)    
    odrive7.set_absolute_position(0)
    odrive8.set_absolute_position(0)
    odrive9.set_absolute_position(0)
    await asyncio.sleep(0.2)
    print("Calibration Complete")

async def main():
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

    odrive5 = pyodrivecan.ODriveCAN(5, canBusID="can1")
    odrive5.initCanBus()
    
    odrive6 = pyodrivecan.ODriveCAN(6, canBusID="can1")
    odrive6.initCanBus()
    
    odrive7 = pyodrivecan.ODriveCAN(7, canBusID="can1")
    odrive7.initCanBus()

    odrive8 = pyodrivecan.ODriveCAN(8, canBusID="can1")
    odrive8.initCanBus()
    
    odrive9 = pyodrivecan.ODriveCAN(9, canBusID="can1")
    odrive9.initCanBus()
        
    # Configure each ODrive
    for odrive in (odrive0, odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9):
        odrive.set_limits(velocity_limit=velocity_limit, current_limit=current_limit)
        time.sleep(0.2)
        odrive.clear_errors(identify=False)
        await asyncio.sleep(0.2)
        odrive.set_controller_mode(control_mode_name="position_control", input_mode_name="pos_filter")
        await asyncio.sleep(0.5)  # Delay to prevent command overlap on CAN bus

    await calibrate(odrive0, odrive1, odrive2, odrive3, odrive4, odrive5, odrive6, odrive7, odrive8, odrive9)

    #Calibrate first time O-Drive is powered up. Comment controller and get_socket.  
    #Then comment out, if O-Drive is powered off, must calibrate again.
    #await calibrate(odrive1, odrive2, odrive3)
    input("press any key to move motors to zero") 
    odrive0.set_position(0)
    odrive1.set_position(0)
    odrive2.set_position(0)
    odrive3.set_position(0)
    
    odrive4.set_position(0)
    odrive5.set_position(0)
    odrive6.set_position(0)
    
    odrive7.set_position(0)
    odrive8.set_position(0)
    odrive9.set_position(0)
    
    await asyncio.sleep(2)
    counter = 1



if counter == 0:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program terminated with keyboard interrupt.")
