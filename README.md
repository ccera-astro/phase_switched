# phase_switched
A simple, single-receiver phase-switched interferometer flow

This flow-graph implements the back-end of a phased-switched interferometer.

It uses a single RTL-SDR by default, and uses the RTS/DTR lines on a serial port
  (default /dev/ttyUSB0) to allow control signals for an external phase-switch.

