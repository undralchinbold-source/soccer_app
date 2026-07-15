# ⚽ Soccer Ball Detector

YOLO загвар ашиглан зураг дээрх хөлбөмбөгийг илрүүлдэг Flask веб аппликейшн.
A Flask web application that detects a soccer ball in an image using a YOLO object-detection model.

Хэрэглэгч зураг (файлаар эсвэл URL-аар) илгээхэд систем түүнийг YOLO загвараар боловсруулж, бөмбөг илэрсэн эсэхийг **бодит хугацаанд** ("Бөмбөг олдлоо!" / "Олдсонгүй") вэб хуудсан дээр харуулна.

---

## 📁 Төслийн бүтэц / Project Structure

```
soccer_app/
├── app.py                  # Flask сервер, API route-ууд (/, /detect, /output/<file>)
├── requirements.txt        # Python dependency жагсаалт
├── models/
│   └── best.pt              # Сургагдсан YOLO жин (model weights)
├── src/
│   ├── __init__.py
│   └── soccer_detection.py  # Илрүүлэлтийн үндсэн логик (OpenCV + YOLO)
├── templates/
│   └── index.html           # Веб UI (upload/URL хэлбэр, үр дүн харуулах)
├── uploads/                  # Хэрэглэгчийн оруулсан зурагнууд хадгалагдах хавтас
└── output/
    └── detected.jpg          # Илрүүлэлтийн үр дүн (bounding box-той зураг)
```

---

## 🛠️ Ашигласан технологи / Tech Stack

| Технологи | Зориулалт |
|---|---|
| **Python 3** | Гол хэл / Core language |
| **Flask** | Веб сервер ба REST API |
| **OpenCV** (`opencv-python`) | Зураг унших, боловсруулах, bounding box зурах |
| **PyTorch** | YOLO загварын суурь framework |
| **YOLO** (`ultralytics`) | Хөлбөмбөгийг илрүүлэх object detection загвар |

---

## ✨ Гол онцлогууд / Key Features

- ⚽ **Бодит хугацааны илрүүлэлт** — зураг илгээмэгц YOLO загвар ажиллаж, "✅ Бөмбөг олдлоо!" эсвэл "❌ Олдсонгүй" гэсэн үр дүнг шууд вэб дээр харуулна.
  Real-time detection — as soon as an image is submitted, the YOLO model runs and the page instantly shows **"Ball found!"** or **"Not found"**.
- 🖼️ **Зураг боловсруулалт** — илэрсэн бөмбөгийг ногоон дөрвөлжин (bounding box) болон итгэлцлийн хувиар (confidence score) тэмдэглэж, `output/detected.jpg` файлд хадгална.
  Image processing — detected balls are marked with a bounding box and confidence score, saved to `output/detected.jpg`.
- 📤 **Файл эсвэл URL-аар оруулах** — компьютероос зураг сонгох, эсвэл интернэт дэх зургийн URL холбоос өгөх боломжтой.
  Supports both file upload and image URL as input.
- 🌐 **Энгийн, хариу үйлдэлтэй веб интерфейс** — Tailwind CSS ашигласан, drag-and-drop маягийн upload UI.
  Simple, responsive web UI built with Tailwind CSS.

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

### 4. Аппликейшныг ажиллуулах / Run the application

```bash
python app.py
```

Сервер амжилттай асвал доорх хаягаар нэвтэрнэ / Once running, open your browser at:

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
