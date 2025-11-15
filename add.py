from flask import Flask
import os

# Створюємо екземпляр додатку
app = Flask(__name__)

@app.route('/')
def hello():
    # Беремо ім'я з "змінної оточення" або ставимо за замовчуванням
    name = os.environ.get('NAME', 'World')
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Запускаємо веб-сервер на всіх IP-адресах, доступних хосту
    app.run(host='0.0.0.0', port=5000)