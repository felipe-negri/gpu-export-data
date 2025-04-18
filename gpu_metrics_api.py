from flask import Flask, jsonify
from pynvml import (
    nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetUtilizationRates,
    nvmlDeviceGetMemoryInfo, nvmlDeviceGetTemperature, nvmlDeviceGetFanSpeed,
    nvmlDeviceGetClockInfo, NVML_TEMPERATURE_GPU, NVML_CLOCK_GRAPHICS
)

app = Flask(__name__)
nvmlInit()
gpu = nvmlDeviceGetHandleByIndex(0)

@app.route("/gpu-stats")
def gpu_metrics():
    util = nvmlDeviceGetUtilizationRates(gpu)
    mem = nvmlDeviceGetMemoryInfo(gpu)
    temp = nvmlDeviceGetTemperature(gpu, NVML_TEMPERATURE_GPU)  # Temperatura da GPU
    fan_speed = nvmlDeviceGetFanSpeed(gpu)  # Velocidade do ventilador (%)
    freq = nvmlDeviceGetClockInfo(gpu, NVML_CLOCK_GRAPHICS)  # Frequência do clock (MHz)

    return jsonify({
        "load": float(util.gpu),                           # Uso da GPU em %
        "memory_percentage": float((mem.used / mem.total) * 100),  # Uso de memória em %
        "memory_used_mb": float(mem.used / 1024**2),       # Memória usada (MB)
        "total_memory_mb": float(mem.total / 1024**2),     # Memória total (MB)
        "temperature": float(temp),                        # Temperatura da GPU (°C)
        "fps": -1,                                         # FPS (não disponível na NVML diretamente)
        "fan_percent": float(fan_speed),                   # Velocidade do ventilador (%)
        "freq_ghz": float(freq / 1000)                     # Frequência do clock (GHz)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)