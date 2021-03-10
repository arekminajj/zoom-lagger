import psutil
import time
somepid = 22108
p = psutil.Process(somepid)
p.suspend()
time.sleep(5)
p.resume()