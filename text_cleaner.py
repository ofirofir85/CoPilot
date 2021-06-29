from base_module import BaseModule
from module_utils import show_popup, get_copied_data, put_in_paste

ALPHA = 'alpha'
PUNCT = 'punctuation'
SPACE = "space"
IS_USER_LIST_ACTIVATED = 'Is user list activated'
USER_LIST = "user list"
PUNCT_LIST = ['/', '\\', ',', '.', ';', '-', '_',"#","^","&","(",")"]

class TextCleaner(BaseModule):
    def __init__(self):
        super().__init__({ALPHA:True, PUNCT:False, SPACE:False, IS_USER_LIST_ACTIVATED:False, USER_LIST:'g J j G'})

    def run(self):
        txt = get_copied_data()
        print(txt)
        if not self.config[ALPHA]:
            txt = "".join(e for e in txt if not e.isalnum())
        if not self.config[PUNCT]:
            txt = "".join(e for e in txt if not e in PUNCT_LIST)
        if not self.config[SPACE]:
            txt = "".join(e for e in txt if not e.isspace())
        if not self.config[IS_USER_LIST_ACTIVATED]:
            user_list = self.config[USER_LIST].split(' ')
            print (user_list)
            txt = "".join(e for e in txt if not e in user_list)


        show_popup('Cleaned Text', txt)
        put_in_paste(txt)