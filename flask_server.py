import json, os
from flask import Flask, render_template, request, session, escape, jsonify
from werkzeug.utils import secure_filename
# import classifier, similar, rnn_lstm
import connect_db

# HTTP 서버 실행하기
UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

color_list = ['베이지색', '검정색', '갈색', '회색', '초록색', '파란색', '빨간색', '하얀색']
cloth_list = ['긴팔티셔츠', '셔츠', '맨투맨_후드', '면바지', '반바지', '반팔', '블라우스', 
 '스커트', '원피스', '청바지', '카디건', '트레이닝복']

# web 렌더링
@app.route("/", methods=['GET'])
def index() :
  return render_template('index.html')

@app.route("/upload", methods=['GET','POST'])
def upload() :
  return render_template('upload.html')

@app.route("/register", methods=['GET', 'POST'])
def register() :
  if request.method == 'POST':

    return 'file uploaded successfully'

  return render_template('register.html')

@app.route("/login", methods=['GET'])
def login() :
  return render_template('login.html')

@app.route("/product", methods=['GET'])
def product() :
  return render_template('product.html')

@app.route("/categories", methods=['GET'])
def categories() :
  return render_template('categories.html')

# # app 부분
# @app.route('/cnn_process', methods=['GET','POST'])
# def cnn_process():
#   # file과 file 이름 가져오기
#   f = request.files['file']
#   # print(f)
#   filename = secure_filename(f.filename)

#   # CNN으로 옷 종류, 색깔 판별
#   # json은 numpy type 못받으므로 int로 형변환
#   cloth = int(classifier.get_cloth(f))
#   color = int(classifier.get_color(f))

#   # 옷 종류와 색깔 json으로 dump
#   return json.dumps({
#     "cloth": cloth,
#     "color": color
#   })

# @app.route('/cosine_process', methods=['GET','POST'])
# def cosine_process():
#   # file 가져오기
#   f2 = request.files['file']

#   # Json으로 Post받은 카테고리 가져오고 int로 변환
#   category = int(request.form.get("category"))

#   # cosine 유사도로 비슷한 이미지의 가격정보 가져오기
#   result = similar.get_similar(f2, category)
#   # print(category)
#   # print(result)

#   # 최대, 최소, 평균 가격 json으로 dump
#   return json.dumps({
#     "max": result[0],
#     "min": result[1],
#     "mean": result[2],
#     "img1": result[3][0],
#     "img2": result[3][1],
#     "img3": result[3][2]
#   })

# @app.route('/rnn_process', methods=['GET','POST'])
# def rnn_process():

#   # Json으로 Post받은 카테고리 가져오고 int로 변환
#   data = request.get_json() 
#   category = int(data['category'])

#   # category를 문자로 바꿈
#   category = cloth_list[category]
#   print(category)

#   # 카테고리를 시드로 문장 생성
#   result = rnn_lstm.generate_text(category)
#   print(result)
  
#   # 생성한 문장 json으로 dump
#   return json.dumps({
#   "text": result
#   })

# @app.route('/upload_process', methods=['GET','POST'])
# def upload_process():

#   # form에서 이미지 받아오기
#   f3 = request.files['file']

#   # 이미지 이름 가져오기
#   filename = secure_filename(f3.filename)

#   # form data 받아오기
#   q = request.form
#   user = 1
  
#   # db에 업로드하기
#   connect_db.query(connect_db.upload(q['title'],int(q['price']),q['contents'],q['deliver'],
#                   q['status'],color_list[int(q['color'])],q['washing'],q['size'],user,int(q['category'])))
#   query = connect_db.query_select(connect_db.select_img_id())

#   img_id = int(query['pd_id'])

#   print(filename)
#   filename = str(img_id) + '.jpg'
#   print(filename)

#   # 업로드 ( .save(경로) )
#   img_url = os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\','/')
#   f3.save(img_url) 
#   size = os.stat(os.path.join(app.config['UPLOAD_FOLDER'], filename)).st_size
  
#   connect_db.query(connect_db.upload_image(img_id, 1, img_url, 'jpg', size))
              
#   return render_template('upload_complete.html')


# 서버 구동
if __name__ == '__main__':
  app.run(host="0.0.0.0", port="8080")

