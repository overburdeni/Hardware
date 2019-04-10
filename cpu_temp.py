import os,time
while True:
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp = dev.read()[5:-3]
    cpu_temp = float(cpu_temp)
    print(cpu_temp)
    time.sleep(1)