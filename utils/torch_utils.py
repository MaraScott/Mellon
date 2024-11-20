import torch
from torchvision.transforms import v2 as tt
from PIL import Image

def list_devices():
    host = ""  # TODO: support multiple hosts

    devices = {}
    default_device = None
    cpu = {
        "index": 0,
        "device": "cpu",
        "host": host,
        "label": (host) + "cpu",
        #"name": "CPU"
    } # TODO: probably need to support multiple cpus

    if torch.cuda.is_available():
        for i in range(torch.cuda.device_count()):
            key = f"{host}cuda:{i}"

            if default_device is None:
                default_device = key

            devices[key] = {
                "index": i,
                "device": f"cuda:{i}",
                "host": host,
                "label": (host) + f"cuda:{i}",
                #"name": f"{torch.cuda.get_device_properties(i).name}"
            }

        devices[f"{host}.cpu"] = cpu

    elif torch.mps.is_available():
        key = f"{host}mps"
        default_device = key
        devices[key] = {
            "index": 0,
            "device": "mps",
            "host": host,
            "label": (host) + "mps",
            #"name": "MPS"
        }

    else:
        key = f"{host}.cpu"
        default_device = key
        devices[key] = cpu

    return devices, default_device

device_list, default_device = list_devices()

def toTensor(image: Image.Image):
    return tt.PILToTensor()(image) / 255.0

def toPIL(tensor: torch.Tensor):
    return tt.ToPILImage()(tensor.clamp(0, 1))