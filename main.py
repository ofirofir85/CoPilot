import MyModule

def main():
    mm = MyModule()
    keyboard.add_hotkey(mm.config['hot_key'], mm.run)
    keyboard.wait('esc')

if __name__ == '__main__':
    main()    