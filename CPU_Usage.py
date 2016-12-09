import psutil
# blocking
psutil.cpu_percent(interval=1)
2.0
# non-blocking (percentage since last call)
psutil.cpu_percent(interval=None)
2.9
# blocking, per-cpu
psutil.cpu_percent(interval=1, percpu=True)
[2.0, 1.0]

print psutil.cpu_percent