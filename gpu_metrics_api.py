from flask import Flask, jsonify
from pynvml import nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetUtilizationRates, nvmlDeviceGetMemoryInfo

app = Flask(__name__)
nvmlInit()
gpu = nvmlDeviceGetHandleByIndex(0)

@app.route("/gpu")
def gpu_metrics():
    util = nvmlDeviceGetUtilizationRates(gpu)
    mem = nvmlDeviceGetMemoryInfo(gpu)
    return jsonify({
        "gpu_util": util.gpu,                  # uso da GPU em %
        "gpu_mem_used": mem.used // 1024**2,   # memória usada (MB)
        "gpu_mem_total": mem.total // 1024**2  # memória total (MB)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
