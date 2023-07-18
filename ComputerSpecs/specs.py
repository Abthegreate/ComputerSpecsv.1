import psutil
import GPUtil

def get_gpu_info():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        gpu = gpus[0]
        return f"{gpu.name}, {gpu.memoryTotal}MB"
    except ImportError:
        return "GPU information not available"

def get_cpu_info():
    cpu_info = []
    cpu_info.append(f"Physical cores: {psutil.cpu_count(logical=False)}")
    cpu_info.append(f"Total cores: {psutil.cpu_count(logical=True)}")
    cpu_info.append(f"Max frequency: {psutil.cpu_freq().max:.2f}Mhz")
    cpu_info.append(f"CPU usage: {psutil.cpu_percent()}%")
    return "\n".join(cpu_info)

def get_ram_info():
    ram = psutil.virtual_memory()
    ram_info = []
    ram_info.append(f"Total: {ram.total//(1024**3)}GB")
    ram_info.append(f"Available: {ram.available//(1024**3)}GB")
    ram_info.append(f"Used: {ram.used//(1024**3)}GB")
    ram_info.append(f"Percentage: {ram.percent}%")
    return "\n".join(ram_info)

def get_storage_info():
    partitions = psutil.disk_partitions()
    storage_info = []
    for partition in partitions:
        storage = psutil.disk_usage(partition.mountpoint)
        storage_info.append(f"Device: {partition.device}")
        storage_info.append(f"Mountpoint: {partition.mountpoint}")
        storage_info.append(f"File system type: {partition.fstype}")
        storage_info.append(f"Total size: {storage.total//(1024**3)}GB")
        storage_info.append(f"Used: {storage.used//(1024**3)}GB")
        storage_info.append(f"Free: {storage.free//(1024**3)}GB")
        storage_info.append(f"Percentage: {storage.percent}%")
        storage_info.append("--------------------------------------")
    return "\n".join(storage_info)

def print_system_info():
    print("GPU Information:")
    print(get_gpu_info())
    print("\nCPU Information:")
    print(get_cpu_info())
    print("\nRAM Information:")
    print(get_ram_info())
    print("\nStorage Information:")
    print(get_storage_info())

print_system_info()
input()
