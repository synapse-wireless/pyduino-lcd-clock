"""Pyduino Alarm Clock Example
This example is a simple application of using the LCD and real-time-clock libraries

Note: The Pyduino is not designed with battery back-up so the clock must be reset when power is applied.

Note: The Portal script, "Portal_Pyduino_Helper.py" can be used to set the time automatically, based on
      your computers clock.

"""

from snappyatmega.rtc import *
from pyduinolcd import *

# IO pins
BUZZER = D0

# Global variables
beep_delay = 0
clock_flash = 0

@setHook(HOOK_STARTUP)
def startup():
    """Startup event to initialize the IO and LCD display"""  
    # Initialize buzzer IO
    writePin(BUZZER, True)
    setPinDir(BUZZER, True)
    
    # Send the commands to initialize the display
    lcd_init()
    
    # Initialize timers to configure the real-time clock
    timer_init(TMR5, WGM_FASTPWM16_TOP_ICR, CLK_FOSC_DIV1024, 0x3d09)
    
    # Clear the screen
    clear_screen()
    
@setHook(HOOK_100MS)
def Timer_100ms():
    """Timer event to keep track of time, drive the buzzer, and check for button presses"""
    global rtc_alarm
    global beep_delay
    
    if rtc_alarm:
        # Dismiss the alarm if any buttons are being pressed
        if check_button() != '':
            clear_alarm()
            
        # Make the typical alarm clock sound
        if beep_delay < 4:
            pulsePin(BUZZER, 50, False)
        elif beep_delay == 8:
            beep_delay = 0
        beep_delay +=1
        
    # Execute one time when alarm event happens
    if rtc_alarm == 1:
        rtc_alarm+=1
        clear_screen()
        write_line1('Press a button  ')
        write_line2('to dismiss      ')
        
        # Broadcast to enable relay 2 on a remote relay shield
        mcastRpc(1, 2, 'set_relay', 2, 1)
        
    # Clock timer keeper function
    if time_str != START_TIME:
        clock_timer_100ms()

@setHook(HOOK_1S)
def Timer_1S():
    """Timer event to update the LCD display"""
    global clock_flash
    if time_str != START_TIME:
        if not rtc_alarm:
            write_line1('Time: ' + get_hours())
            write_line2('Date: '+ get_date())
    else:
        clock_flash+=1
        if clock_flash&1:
            write_line1('Time: 12:00:00')
        else:
            write_line1('Time:         ')
    
def set_clock(month, day, year, hour, minute, second):
    """Set the current time"""
    rtc_set_time(month, day, year, hour, minute, second)
    
def set_alarm_time(month, day, year, hour, minute, second):
    """Set the desired alarm event time"""
    rtc_set_alarm(month, day, year, hour, minute, second)
    
def clear_alarm():
    """Clear the alarm event"""
    # Broadcast to disable relay 2 on a remote relay shield
    mcastRpc(1, 2, 'set_relay', 2, 0)
    rtc_clear_alarm()