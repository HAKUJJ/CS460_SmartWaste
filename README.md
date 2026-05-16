# ♻️ Smart Waste Detective AI (Fusion Edition)
Project for CS460 - [ใส่ชื่อโปรเจกต์ภาษาไทยหรืออังกฤษ]

โปรเจกต์นี้คือ AI ผู้ช่วยแยกขยะอัจฉริยะ โดยใช้เทคนิค Feature Fusion ในการรวมโมเดลผู้เชี่ยวชาญด้านขยะ (12 คลาส) และโมเดลผู้เชี่ยวชาญด้านสัตว์ (ป้องกันการทิ้งสิ่งมีชีวิต) เข้าด้วยกัน ทำให้สามารถแยกประเภทสิ่งของและแนะนำถังขยะที่ถูกต้องได้อย่างแม่นยำ

## 📂 ไฟล์ที่สำคัญใน Repository นี้
- `app.py`: Source code สำหรับรัน Web Application ด้วย Gradio
- `train_model.ipynb`: โค้ดสำหรับเทรนโมเดลบน Kaggle
- `CS460_SmartWaste.pdf`: สไลด์นำเสนอโปรเจกต์ (Presentation Slide)

## 🔗 ลิงก์สำหรับดาวน์โหลดโมเดล
เนื่องจากไฟล์โมเดลมีขนาดใหญ่ จึงฝากไว้ที่ Google Drive:
- [ดาวน์โหลดไฟล์ fusion_smart_waste.keras ที่นี่](ใส่ลิงก์ Google Drive ของคุณตรงนี้) 
*(เมื่อดาวน์โหลดแล้ว ให้นำมาวางไว้ในโฟลเดอร์เดียวกับ app.py)*

## 🛠️ วิธีการติดตั้งและรันโค้ด (Setup & Run Commands)

1. **Clone repository นี้ลงเครื่อง:**
   ```bash
   git clone [https://github.com/ช](https://github.com/ช)ื่อผู้ใช้ของคุณ/CS460_SmartWaste.git
   cd CS460_SmartWaste
