# ⚽ Soccer Ball Detector

YOLO загвар ашиглан зураг дээрх хөлбөмбөгийг илрүүлдэг Flask веб аппликейшн.
A Flask web application that detects a soccer ball in an image using a YOLO object-detection model.

Хэрэглэгч зураг (файлаар эсвэл URL-аар) илгээхэд систем түүнийг YOLO загвараар боловсруулж, бөмбөг илэрсэн эсэхийг **бодит хугацаанд** ("Бөмбөг олдлоо!" / "Олдсонгүй") вэб хуудсан дээр харуулна.
When a user submits an image (either as a file or a URL), the system processes it with the YOLO model and shows, **in real time**, whether a ball was found ("Ball found!" / "Not found") right on the web page.

---

## 📁 Төслийн бүтэц / Project Structure

```
soccer_app/
├── app.py                    # Flask сервер, API route-ууд (/, /detect, /output/<file>)
│                              # Flask server, API routes (/, /detect, /output/<file>)
├── requirements.txt          # Python dependency жагсаалт
│                              # Python dependency list
├── models/
│   └── best.pt                # Сургагдсан YOLO жин (model weights)
│                               # Trained YOLO model weights
├── src/
│   ├── __init__.py
│   └── soccer_detection.py    # Илрүүлэлтийн үндсэн логик (OpenCV + YOLO)
│                               # Core detection logic (OpenCV + YOLO)
├── templates/
│   └── index.html              # Веб UI (upload/URL хэлбэр, үр дүн харуулах)
│                                # Web UI (upload/URL form, result display)
├── uploads/                    # Хэрэглэгчийн оруулсан зурагнууд хадгалагдах хавтас
│                                # Folder where user-uploaded images are stored
└── output/
    └── detected.jpg             # Илрүүлэлтийн үр дүн (bounding box-той зураг)
                                  # Detection result (image with bounding box)
```

---

## 🛠️ Ашигласан технологи / Tech Stack

| Технологи / Technology | Зориулалт / Purpose |
|---|---|
| **Python 3** | Гол хэл / Core language |
| **Flask** | Веб сервер ба REST API / Web server and REST API |
| **OpenCV** (`opencv-python`) | Зураг унших, боловсруулах, bounding box зурах / Reading, processing images and drawing bounding boxes |
| **PyTorch** | YOLO загварын суурь framework / Underlying framework for the YOLO model |
| **YOLO** (`ultralytics`) | Хөлбөмбөгийг илрүүлэх object detection загвар / Object detection model used to detect the soccer ball |

---

## ✨ Гол онцлогууд / Key Features

- ⚽ **Бодит хугацааны илрүүлэлт / Real-time detection** — зураг илгээмэгц YOLO загвар ажиллаж, "✅ Бөмбөг олдлоо!" эсвэл "❌ Олдсонгүй" гэсэн үр дүнг шууд вэб дээр харуулна.
  As soon as an image is submitted, the YOLO model runs and the page instantly shows **"✅ Ball found!"** or **"❌ Not found"**.
- 🖼️ **Зураг боловсруулалт / Image processing** — илэрсэн бөмбөгийг ногоон дөрвөлжин (bounding box) болон итгэлцлийн хувиар (confidence score) тэмдэглэж, `output/detected.jpg` файлд хадгална.
  Detected balls are marked with a green bounding box and a confidence score, then saved to `output/detected.jpg`.
- 📤 **Файл эсвэл URL-аар оруулах / Upload by file or URL** — компьютероос зураг сонгох, эсвэл интернэт дэх зургийн URL холбоос өгөх боломжтой.
  Supports both uploading an image from your computer and providing an image URL from the internet.
- 🌐 **Энгийн, хариу үйлдэлтэй веб интерфейс / Simple, responsive web UI** — Tailwind CSS ашигласан, drag-and-drop маягийн upload UI.
  Built with Tailwind CSS, featuring a clean, drag-and-drop-style upload interface.

---

## 🚀 Суулгах ба ажиллуулах / Installation & Usage

### 1. Repository татах / Clone the repository

```bash
git clone <repo-url>
cd soccer_app
```

### 2. Виртуал орчин үүсгэх (venv) / Create a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> 💡 Виртуал орчинг идэвхжүүлснийг терминалын мөрөнд `(venv)` гэж харагдахаас мэдэж болно.
> You'll know the virtual environment is active when you see `(venv)` in your terminal prompt.

### 3. Шаардлагатай сангуудыг суулгах / Install dependencies

```bash
pip install -r requirements.txt
```

Энэ команд нь Flask, OpenCV, PyTorch, Ultralytics (YOLO) зэрэг бүх шаардлагатай Python сангуудыг `requirements.txt`-д заасны дагуу суулгана.
This command installs all required Python packages — Flask, OpenCV, PyTorch, Ultralytics (YOLO), etc. — as pinned in `requirements.txt`.

### 4. Аппликейшныг ажиллуулах / Run the application

```bash
python app.py
```

Сервер амжилттай асвал доорх хаягаар нэвтэрнэ / Once the server is running, open your browser at:

```
http://127.0.0.1:8000
```

### 5. Ашиглах / How to use

1. Веб хуудсан дээр зураг сонгож **"Файлаар таних"** товч дар, эсвэл зургийн URL оруулж **"URL-аар таних"** дар.
   On the page, upload an image and click **"Detect by file"**, or paste an image URL and click **"Detect by URL"**.
2. Систем YOLO загвараар боловсруулаад үр дүнг шууд харуулна: ✅ **"Бөмбөг олдлоо!"** (bounding box-той зурагтай) эсвэл ❌ **"Олдсонгүй"**.
   The system processes the image and instantly shows the result: ✅ **"Ball found!"** (with the marked image) or ❌ **"Not found"**.

---

## 📌 Тэмдэглэл / Notes

- YOLO загварын жин (`models/best.pt`) урьдчилан сургагдсан байх шаардлагатай.
  The YOLO model weights (`models/best.pt`) must already be trained/present before running.
- `uploads/` болон `output/` хавтаснууд ажиллах явцад автоматаар ашиглагдана.
  The `uploads/` and `output/` folders are used automatically at runtime for input and result images.
- Виртуал орчин (`venv/`) болон Python bytecode кэш (`__pycache__/`) хавтаснууд `.gitignore`-д орсон тул хувилбар удирдлагад ороогүй.
  The virtual environment (`venv/`) and Python bytecode cache (`__pycache__/`) folders are listed in `.gitignore` and are excluded from version control.
