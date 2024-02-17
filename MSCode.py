from flask import Flask, render_template
from SimConnect import *
import json

app = Flask(__name__)

# Создание объекта SimConnect
sc = SimConnect()

# Определение структуры данных для получения информации о положении самолета
class PlaneData:
    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.altitude = None

# Callback-функция для обработки данных о положении самолета
def plane_pos_callback(data):
    plane_data.latitude = data.Latitude
    plane_data.longitude = data.Longitude
    plane_data.altitude = data.Altitude

# Определение структуры данных для передачи информации о положении самолета на веб-страницу
class PositionData:
    def __init__(self, latitude, longitude, path):
        self.latitude = latitude
        self.longitude = longitude
        self.path = path

# Маршрутные точки для отображения пройденного пути
path = []

# Callback-функция для обработки данных о пройденном пути
def plane_path_callback(data):
    position_data = PositionData(data.Latitude, data.Longitude, path.copy())
    socketio.emit('position_update', json.dumps(position_data.__dict__))

# Функция для обработки сообщений от SimConnect
def dispatch_message(sc):
    sc.dispatch(
        [
            (SimConnectRecvId.SIMOBJECT_DATA, plane_pos_callback),
            (SimConnectRecvId.SIMOBJECT_DATA_BYTYPE, plane_path_callback),
        ]
    )

# Маршрут для отображения веб-страницы
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket для передачи данных на веб-страницу
@socketio.on('connect')
def test_connect():
    global path
    path = []  # сброс пройденного пути при подключении нового клиента

# Запуск приложения Flask с использованием SocketIO
if __name__ == '__main__':
    plane_data = PlaneData()
    sc.call_dispatch(dispatch_message)
    socketio.run(app, host='0.0.0.0', port=5000)


