import torch
print("CUDA是否可用:", torch.cuda.is_available())
print("CUDA版本:", torch.version.cuda)
print("当前设备:", torch.cuda.current_device())
print("设备数量:", torch.cuda.device_count())
print("设备名称:", torch.cuda.get_device_name(0))