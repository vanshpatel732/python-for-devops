import psutil

def get_threshold_values():
    cpu_thres = int (input("Get the CPU usage threshold: "))
    disk_thres = int (input("Get the Disk usage threshold: "))
    mem_thres = int (input("Get the Memory usage threshold: "))
    return cpu_thres, disk_thres, mem_thres

def check_system_health(cpu_thres, disk_thres, mem_thres):
    current_cpu = psutil.cpu_percent(interval=1)
    current_disk = psutil.disk_usage('/').percent
    current_mem = psutil.virtual_memory().percent

    if current_cpu > cpu_thres:
        print("CPU usage is above the threshold: ", current_cpu)
    else:
        print("CPU usage is below the threshold: ", current_cpu)

    if current_disk > disk_thres:
        print("Disk usage is above the threshold: ", current_disk)
    else:
        print("Disk usage is below the threshold: ", current_disk)

    if current_mem > mem_thres:
        print("Memory usage is above the threshold: ", current_mem)
    else:
        print("Memory usage is below the threshold: ", current_mem)

cpu_thres, disk_thres, mem_thres = get_threshold_values()
check_system_health(cpu_thres, disk_thres, mem_thres)
