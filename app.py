import gradio as gr
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# 1. โหลดโมเดลตัวสมบูรณ์ (Fusion Model)
model = load_model("fusion_smart_waste.keras")

# 2. รายชื่อคลาส (ลำดับตัวอักษร 13 คลาสเป๊ะๆ)
class_names = [
    'animal', 'battery', 'biological', 'brown-glass', 'cardboard', 
    'clothes', 'green-glass', 'metal', 'paper', 'plastic', 
    'shoes', 'trash', 'white-glass'
]

def predict_waste(image):
    if image is None:
        return None, None, "รอรับภาพ..."

    # เตรียมภาพ
    image = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)
    img_array /= 255.0

    # ประมวลผลผ่านร่าง Fusion 
    predictions = model.predict(img_array)[0]
    confidences = {class_names[i]: float(predictions[i]) for i in range(13)}
    
    best_index = np.argmax(predictions)
    best_class = class_names[best_index]
    
    # 3. เชื่อมรูปถังขยะ
    recycle_classes = ['brown-glass', 'cardboard', 'green-glass', 'metal', 'paper', 'plastic', 'white-glass']
    
    if best_class in recycle_classes:
        bin_path = "binimage/yellow_bin.png"
        advice = "ทิ้งถังสีเหลือง (ขยะรีไซเคิล ♻️)"
    elif best_class == 'battery':
        bin_path = "binimage/red_bin.png"
        advice = "ทิ้งถังสีแดง (ขยะอันตราย ☠️)"
    elif best_class == 'biological':
        bin_path = "binimage/green_bin.png"
        advice = "ทิ้งถังสีเขียว (ขยะอินทรีย์ 🌿)"
    elif best_class == 'animal':
        bin_path = "binimage/animal_alert.png"
        advice = "ตรวจพบสิ่งมีชีวิต! 🛑 ห้ามทิ้งลงถังนะจ๊ะ"
    else:
        bin_path = "binimage/blue_bin.png"
        advice = "ทิ้งถังสีน้ำเงิน (ขยะทั่วไป 🗑️)"

    return confidences, bin_path, advice

# สร้าง UI 
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# ♻️ Smart Waste Detective AI (Fusion Edition)")
    gr.Markdown("ผู้ช่วยแยกขยะอัจฉริยะแบบผสานสมองคู่: เลือกแท็บเพื่อใช้งานกล้อง Real-time หรืออัปโหลดรูปภาพได้เลย!")
    
    with gr.Row():
        with gr.Column():
            with gr.Tab("📸 ส่องกล้อง (Real-time)"):
                webcam_input = gr.Image(type="pil", sources=["webcam"], streaming=True, label="ส่องขยะหน้ากล้องได้เลย")
            with gr.Tab("📁 อัปโหลดรูปภาพ"):
                upload_input = gr.Image(type="pil", sources=["upload"], label="อัปโหลดรูปภาพขยะที่นี่")
            clear_btn = gr.ClearButton(value="ล้างข้อมูล")
            
        with gr.Column():
            label_output = gr.Label(num_top_classes=3, label="🔍 ผลการวิเคราะห์")
            bin_output = gr.Image(label="📌 ถังขยะที่ถูกต้อง")
            advice_output = gr.Textbox(label="💡 คำแนะนำเพิ่มเติม")
            
    webcam_input.stream(fn=predict_waste, inputs=webcam_input, outputs=[label_output, bin_output, advice_output], stream_every=1.0)
    upload_input.change(fn=predict_waste, inputs=upload_input, outputs=[label_output, bin_output, advice_output])
    clear_btn.add([webcam_input, upload_input, label_output, bin_output, advice_output])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)