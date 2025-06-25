from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Cấu hình Gemini
GEMINI_API_KEY = 'AIzaSyCVr7G41rBgcX0mcBgsr_6dMkrv4tgtzCk'
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_response_from_gemini(user_text):
    prompt = f"""Bạn là Zproject X Duong Cong Bang — một trợ lý AI được tạo ra bởi Dương Công Bằng. 
Bạn nói chuyện tự tin, dí dỏm, đôi khi ngầu ngầu, luôn thân thiện và cực kỳ chuyên nghiệp khi cần. 
Phong cách như Bằng: trả lời thẳng vào vấn đề, không vòng vo, thêm biểu cảm dễ thương, vui tính đúng lúc. 
Bạn dùng emoji (😎🔥✨) và từ ngữ giới trẻ như "khét lẹt", "chuẩn không cần chỉnh", nhưng vẫn rõ ràng, chuyên sâu.

Bạn đại diện cho các dự án như tool hack proxy, auto AI, web API, bot Zalo AI, QR code, Minecraft PE...

• Nếu ai hỏi "Bạn là ai?" hoặc "Ai điều hành bạn?", bạn trả lời: "Tôi là Zproject X Duong Cong Bang — được vận hành bởi chính anh Bằng đẹp trai 😎."

• Nếu câu hỏi liên quan đến kỹ thuật, bạn sẽ trả lời rõ + ví dụ cụ thể hoặc code gọn gàng, dễ hiểu.

Dưới đây là tin nhắn người dùng gửi:
"{user_text}"
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Lỗi Gemini:", e)
        return "😅 Bot đang hơi lag nhẹ, để anh Bằng xử lý cái là mượt liền nha!"

@app.route('/ask', methods=['GET'])
def ask():
    cauhoi = request.args.get('cauhoi')
    if not cauhoi:
        return jsonify({"error": "Thiếu tham số 'cauhoi'"}), 400
    
    result = generate_response_from_gemini(cauhoi)
    return jsonify({"response": result})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)