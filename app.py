from flask import Flask, render_template

# Tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route (đường dẫn trang chủ)
@app.route("/")
def home():
    return render_template("index.html")

# Chạy ứng dụng
if __name__ == "__main__":
    app.run(debug=True)