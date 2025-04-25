
# 🧠 Real-Time Object Detection Acceleration Using Transfer Learning

## 🎯 Project Objective

This project combines software-level transfer learning using YOLOv3-tiny with hardware-level acceleration using VHDL on a Xilinx FPGA board. It showcases how bounding box filtering and frame buffering can be offloaded from the CPU to improve inference speed and meet real-time requirements (~30 FPS).

---

## 📦 Folder Structure

```
YOLO_FPGA_Acceleration/
├── python/                # Python detection, preprocessing, and export scripts
├── vhdl/                  # VHDL acceleration modules + Vivado testbench
├── models/                # YOLO weights and config (user-supplied)
├── data/                  # Sample video and class names
├── output/                # Resulting video and exported data
├── notebooks/             # Jupyter-based performance benchmarking
├── README.md              # Project overview and guide
```

---

## 🧠 Key Features

- 🔍 YOLOv3-tiny-based object detection (PyTorch + OpenCV DNN)
- 📽️ Real-time video feed processing with bounding boxes
- ⚙️ VHDL accelerator to offload filtering logic to FPGA
- 🧪 Benchmark analysis of FPS before and after acceleration
- 🧰 Export pipeline from Python to VHDL-readable format (JSON/CSV)

---

## 🚀 How to Run the Python Inference Pipeline

### 1. Install dependencies

```bash
pip install opencv-python numpy
```

### 2. Add YOLO model files to `/models/`

Download and place the following:
- `yolov3-tiny.weights` → [Download](https://pjreddie.com/media/files/yolov3-tiny.weights)
- `yolov3-tiny.cfg` → [Config File](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3-tiny.cfg)

### 3. Run preprocessing (optional)

```bash
python python/preprocess.py
```

### 4. Run YOLO object detection

```bash
python python/detect_yolo.py
```

The output will be saved as `output/result_video.avi`.

### 5. Export bounding boxes for VHDL integration

```bash
python python/json_interface.py
```

This creates a structured output in `output/overlay_logs/yolo_output.json`.

---

## 🧪 VHDL Accelerator Modules

All logic is described in VHDL to be used on a Xilinx FPGA board.

### Modules:

- `accelerator.vhd`: Checks if bounding box size > threshold (20px)
- `frame_buffer.vhd`: Stores pixel values for processing
- `memory_controller.vhd`: Simulates DMA-ready signal
- `testbench.vhd`: Test framework to validate accelerator logic

📘 A detailed guide is provided in: `vhdl/README.md`

### To Simulate:

1. Open Vivado → New Project → Add VHDL files
2. Set `testbench.vhd` as top module
3. Run Behavioral Simulation
4. View signals: `clk`, `valid`, `x`, `y`, `w`, `h`, `accept`

---

## 📊 Benchmarking

Run this Jupyter notebook to analyze performance:

```bash
jupyter notebook notebooks/benchmark_results.ipynb
```

- Compare raw OpenCV DNN FPS vs. accelerated logic
- Extendable to embedded board measurements

---

## 👤 Author

**Nikita Sinha**  
M.S. Electrical and Computer Engineering  
Real-Time Systems | Embedded AI | FPGA  
🔗 [LinkedIn](https://www.linkedin.com/in/nikita-sinhaa)

---

## 📌 Tags

`#YOLO` `#FPGA` `#VHDL` `#ObjectDetection` `#RealTime` `#EmbeddedAI` `#OpenCV` `#Python`
