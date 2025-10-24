from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Thư mục lưu ảnh upload
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Cho phép upload các định dạng này
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html', title="Trang chủ")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Không có tệp nào được chọn!'
        file = request.files['file']
        if file.filename == '':
            return 'Chưa chọn tệp nào!'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('gallery'))
    return render_template('upload.html', title="Tải lên hình ảnh")

@app.route('/gallery')
def gallery():
    image_files = os.listdir(app.config['UPLOAD_FOLDER'])
    # ✅ chỉ lưu tên file thôi, không thêm /static/uploads
    return render_template('gallery.html', images=image_files, title="Thư viện công trình")
if __name__ == '__main__':
    app.run(debug=True)