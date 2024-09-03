from flask import Flask, request, render_template, session
from dotenv import load_dotenv
import os
from openai import OpenAI
from database import get_db
from sqlalchemy import text
import re

load_dotenv()

app = Flask(__name__)

# 세션을 사용하려면 비밀 키(secret key)를 설정해야 합니다.
app.secret_key = 'abcd1234'  # 실제 앱에서는 이 키를 복잡하고 보안적으로 안전한 값으로 설정하세요.

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

messages = []  # 채팅 내역을 저장하는 리스트

def make_prompt(user_input):
    res = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=user_input
    )
    return res.choices[0].message.content  # dict: 제공

@app.route('/', methods=["GET", "POST"])
def index():
    db = next(get_db())
    
    if request.method == 'POST':
        user_input = request.form['user_input']  # 사용자가 입력한 내용
        
        # 세션에서 'name'과 'email'을 가져오거나 초기화
        name = session.get('name')
        email = session.get('email')

        if user_input in ["안녕", "안녕하세요", "문의"]:
            conversation = [{"role":"system", "content":"You are a very kindful and helpful shopping mall C/S assistant"}]
            conversation.extend([{"role": msg['role'], "content": msg['content']} for msg in messages])
            conversation.append({"role": "user", "content": user_input})
            bot_response = make_prompt(conversation)
       
        else:
            # 세션에 이름과 이메일이 없으면 새로 추출하고 세션에 저장
            if not name or not email:
                name, email = extract_customer_name_email(user_input)
                session['name'] = name
                session['email'] = email
            
            # 고객 정보가 세션에 있는 경우 데이터베이스에서 사용자 확인
            if name and email:
                query = text("SELECT * FROM users WHERE name = :name AND email = :email")
                user = db.execute(query, {"name": name, "email": email}).mappings().fetchone()
                
                if user:
                    bot_response = f"안녕하세요 {user['name']}님! 무엇을 도와드릴까요?"
                    
                    if user_input in ['구매내역']:
                        query = text("SELECT * FROM purchases WHERE user_id = :user_id")
                        purchases = db.execute(query, {'user_id': user['id']}).mappings().fetchall()
                        
                        if purchases:
                            purchase_detail = "\n".join(
                                [f"주문 내역: {p['id']}, 수량: {p['quality']}, 상태: {p['status']}" for p in purchases]
                            )
                            bot_response = f"{user['name']}님의 주문 내역은 다음과 같습니다. {purchase_detail}"
                        
                        else:
                            bot_response = '주문 내역이 확인되지 않습니다.'
                    
                    elif user_input in ['환불요청']:
                        query = text("SELECT * FROM purchases WHERE user_id = :user_id")
                        purchases = db.execute(query, {'user_id': user['id']}).mappings().fetchall()
                        
                        if purchases:
                            purchase_detail = "\n".join(
                                [f"주문 내역: {p['id']}, 수량: {p['quality']}, 상태: {p['status']}" for p in purchases]
                            )
                            bot_response = f"{user['name']}님의 주문 내역은 다음과 같습니다. {purchase_detail}"
                        
                        else:
                            bot_response = '주문 내역이 확인되지 않습니다.'
                
                else:
                    bot_response = "등록된 사용자 정보가 없습니다."
            else:
                bot_response = "이름과 이메일을 다시 입력해주세요."

        messages.append({'role': 'user', 'content': user_input})
        messages.append({'role': 'assistant', 'content': bot_response})
    
    return render_template('index.html', messages=messages)

def extract_customer_name_email(input_text):
    name_pattern = r"[가-힣]+[가-힣]+[가-힣]"
    email_pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"
    name_match = re.search(name_pattern, input_text)
    email_match = re.search(email_pattern, input_text)
    name = name_match.group(0) if name_match else None
    email = email_match.group(0) if email_match else None
    return name, email

if __name__ == "__main__":
    app.run(debug=True)
