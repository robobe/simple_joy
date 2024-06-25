from linux_joystick import AxisEvent, ButtonEvent, Joystick

# Create joystick device (/dev/input/js0)
js = Joystick(0)
while True:
    # Get next event (blocking)
    event = js.poll()
    if isinstance(event, AxisEvent):
        print(f"Axis {event.id} is {event.value}")
    elif isinstance(event, ButtonEvent):
        print(f"Button {event.id} is {event.value}")