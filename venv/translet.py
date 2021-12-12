from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import tkinter as tk
import tkinter.font as tkFont


text_buf = pyperclip.paste()



def translat(text_in1: str) -> str:
    """
    Функция принимает текст на Английском языке и отправлет запрос на google translate
    и возвращает текст на русском языке
    :param text_in: str
    :return: translats_text: str
    """
    option = Options()
    option.headless = True
    driver = Firefox(executable_path='/home/yaroslav/my_project/venv/geckodriver', options=option)
    driver.get(f"https://translate.google.com/?hl=ru&sl=en&tl=ru&text={text_in1}&op=translate")
    try:
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CLASS_NAME, 'J0lOec')))
    except Exception as ex:
        with open('error', 'w') as fail:
            fail.write(str(ex))
            driver.close()
            driver.quit()
    translats_text = driver.find_element_by_class_name('J0lOec').text
    translats_text = ''.join(translats_text.split('\n'))
    print(translats_text)
    driver.close()
    driver.quit()
    return translats_text


def show(text_in2: str) -> None:
    """Функия выводит переданный текст в окне внизу экрана
    :param text:str
    :return: None
    """
    window = tk.Tk()
    h = window.winfo_screenheight()
    w = window.winfo_screenwidth()
    w = w // 2 - 500
    h = h - 250
    window.geometry(f'1000x200+{w}+{h}')
    isert_text = tk.Text(window)
    font_us = tkFont.Font(family='Times New Roman', size=12)
    scroll = tk.Scrollbar(command=isert_text.yview)
    scroll.pack(side='right', fill='y')
    isert_text.config(yscrollcommand=scroll.set,
                      wrap='word',
                      pady=5,
                      padx=10,
                      font=font_us,
                      foreground='#FF1493'
                      )
    isert_text.insert(1.0, text_in2)
    isert_text.config(state='disabled')
    window.title("Переведенный текст")
    isert_text.pack(fill='both')
    window.mainloop()


if __name__ == '__main__':
    translated_text = translat(text_buf)
    show(translated_text)
