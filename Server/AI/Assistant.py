import os
import speech_recognition as sr

#Add libav to PATH
libav_path = os.path.join(os.getcwd(), "AI", "ffmpeg", "bin")
os.environ["PATH"] += libav_path + os.pathsep
from pydub import AudioSegment

from Adafruit_IO import MQTTClient

ADAFRUIT_RELAY_FEED_ID = "group-project.bbc-relay"
ADAFRUIT_LED_FEED_ID = "group-project.bbc-led"
ADAFRUIT_FEED_ID = [ADAFRUIT_RELAY_FEED_ID, ADAFRUIT_LED_FEED_ID]

def connected(client):
    print("Connected succesfully")
    for id in ADAFRUIT_FEED_ID:
        client.subscribe(id)

ADAFRUIT_IO_USERNAME = "Frost984"
ADAFRUIT_IO_KEY = "aio_qJaZ10pZlJnQMxtSk5tDB3v4NYj6"
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected


#TODO: ASSIGMENT
def turn_on_light():
    client.publish(ADAFRUIT_LED_FEED_ID, "1")
    print("Đèn đã được mở!")
    return 0

def turn_off_light():
    client.publish(ADAFRUIT_LED_FEED_ID, "0")
    print("Đèn đã được tắt!")
    return 0

def open_door():
    print("Cửa đã được mở!")
    return 0

def close_door():
    print("Cửa đã được đóng và khóa!")
    return 0

# Speech To Text: Chuyển đổi giọng nói bạn yêu cầu vào thành văn bản
def get_text(file_handle):
    #print("Begin recognizing...")
    r = sr.Recognizer()
    with sr.WavFile(file_handle) as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            return text.lower()
        except:
            print("Can't covert speech to text")
            return None

def convert_to_wav(file_path):
    '''
    Convert .m4a file to .wav format
    :param file_path: .m4a file path
    :return: a handle to .wav file
    '''
    wav_filename = file_path.split(".")[0] + ".wav"
    with open(file_path, "rb") as f:
        track = AudioSegment.from_file(f, format='m4a')
        wav_handle = track.export(wav_filename, format='wav')
        return wav_handle

def exec_voice_command(file_path):
    '''
    Execute voice command from a .m4a file
    :param file_path: path of the audio file that contains the voice command, in .m4a format
    :return:
    '''
    wav_handle = convert_to_wav(file_path)
    converted_text = get_text(wav_handle)
    os.remove(wav_handle.name)
    os.remove(file_path)

    light_on_tokens = ["mở đèn", "bật đèn", "sáng đèn"]
    light_off_tokens = ["tắt đèn", "khóa đèn", "đóng điện"]
    door_open_tokens = ["mở cửa", "cửa ơi mở ra"]
    door_close_tokens = ["đóng cửa", "khóa cửa", "khép cửa"]

    if not converted_text:
        return -1
    elif any([i in converted_text for i in light_on_tokens]):
        return turn_on_light()
    elif any([i in converted_text for i in light_off_tokens]):
        return turn_off_light()
    elif any([i in converted_text for i in door_open_tokens]):
        return open_door()
    elif any([i in converted_text for i in door_close_tokens]):
        return close_door()
