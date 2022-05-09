
import os
from playsound import playsound
import speech_recognition as sr
import time
import speech_recognition
import wikipedia
import datetime
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS

# Khai báo các biến cho quá trình làm Google
wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()
robot_ear = speech_recognition.Recognizer()

# Text To Speech: Chuyển đổi văn bản thành giọng nói
def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound("sound.mp3", False)
    os.remove("sound.mp3")


# Speech To Text: Chuyển đổi giọng nói bạn yêu cầu vào thành văn bản
def get_audio():
    print("\nBot: \tĐang nghe...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=8)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower()
        except:
            print("...")
            return 0

#FIXME: MỘT SỐ CHỨC NĂNG CHÍNH

#TODO: ASSIGMENT
def turnonlight(): #Điều kiện thực hiện câu nói
    speak("Đèn đã được mở!")

def turnofflight():
    speak("Đèn đã được tắt!")

def turnondoor():
    speak("Cửa đã được mở!")

def turnoffdoor():
    speak("Cửa đã được đóng và khóa!")
#TODO:

# Tạm biệt
def stop():
    speak("Tạm biệt, hẹn gặp lại bạn sau!")
    time.sleep(2)


# Tiếp thu âm thanh
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Mình không nghe rõ. Bạn nói lại được không!")
            time.sleep(3)
    time.sleep(2)
    stop()
    return 0


# Xin chào
def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Chúc bạn buổi chiều vui vẻ".format(name))
    else:
        speak("Chào buổi tối bạn {}. Chúc bạn buổi tối bình yên".format(name))
    time.sleep(5)


# Cho biết thời gian hiện tại
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút %d giây' % (now.hour, now.minute, now.second))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")
    time.sleep(4)

# Nunu
def assistant():
    # hello = get_text()
    speak("Xin chào, bạn cần mình giúp gì vậy?")
    time.sleep(5)

    while True:
        text = get_text()
        if not text:
            break
        elif "mở đèn" in text or "bật đèn" in text or "sáng đèn" in text:
            turnonlight()
            with open("turnonlight.txt",'w',encoding = 'utf-8') as f:
                f.write("mở đèn")
        elif "tắt đèn" in text or "khóa đèn" in text or "đóng điện" in text:
            turnofflight()
            with open("turnofflight.txt",'w',encoding = 'utf-8') as f:
                f.write("tắt đèn")
        elif "mở cửa" in text or "cửa ơi mở ra" in text:
            turnondoor()
            with open("turnondoor.txt",'w',encoding = 'utf-8') as f:
                f.write("mở cửa")
        elif "đóng cửa" in text or "khóa cửa" in text or "khép cửa" in text:
            turnoffdoor()
            with open("turnoffdoor.txt",'w',encoding = 'utf-8') as f:
                f.write("đóng cửa")
        elif "dừng" in text or "tạm biệt" in text or "ngủ thôi" in text:
            stop()
            break
        elif "chào" in text:
            hello("Boss")
        elif "giờ" in text or "ngày" in text:
            get_time(text)
        else:
            speak("Bạn cần Bot giúp gì ạ?")
            time.sleep(2)

# Gọi Nunu
assistant()
