import PySimpleGUI as sg
from win10toast import ToastNotifier

toaster = ToastNotifier() #notificacoes

sg.theme('DarkBlack') #tema

#imagens

play = b'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'
stop = b'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'
icone = b'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAQAAAD9CzEMAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QAAKqNIzIAAAAJcEhZcwAADdcAAA3XAUIom3gAAAAHdElNRQflAwIJDSmfOU9kAAAD/klEQVRYw63YS2iUVxQH8F+eTSKJ8RFj42s0iFREoyitVSoKShGxoCtXFcHitqjLULULV4LoTnd1pYIIirYWQitalNhqi6VQiY7GKFqiaF4mmtwuTGYmme9LvqT9z2LmO+fe87/nu/c87pAMqz0Qcj4PrE42sTAhwTqpYc8p6/5fgrIEkv9EMGEkJehNIIlEUYx8kq2+8MyLweduDT7MLKdfs2OeDj4t9JVaj7xN6lWRtc7pFpxXmZEu8Thzhh5bkpFXOi/ods7aqOVGebDbSSuUYL4Wvw9Kgxo3/eiqO/5yWfegfIevFSvxka1e+nXs9Ze6kHPeb6jJLKVKjTp1alRlFlbjRs7oC0pHmivOI+jTZLNC9LnmpE5TNfjYUnNN9QF6vfDIH266o9NRu61VigFN+pLswQzXBH/aqUq9Rrd0DYvioU+XWxrVq/Klu4JrZiTd5m1OmG+mg9IGBs0N6PZcq1bPdedI0w6aab4TtkWZKog5R8U2+NYKBXjnvl/c8LfnelCu1kKf+NQCxQh+06jJO/1JPSizT7sg6PWTnWZHBGSh2Xb6Wa8gaLcvafKgwmE9guCePapHeDzc52p73BMEPQ6rSGK+1AG9ggGXLM3TzjMvT7bUZQOCXgfyj2k+dukU9PtObYR2hx0R0lqn9As67RrL/EppQXDa9Ej9UUcj5dOdFgRpK0czP8nZwfhNRerLNWlSHqlLDcb0WZPiCbbrFrTbFKNPeehhDDmbtAu6bY9f/yVBcCw2iW/Uo8fGGG2RY4LgUpwP670WtFkW6+FeQbA3Vr9Mm+C19VlRbgBtVokr7sZML7QcLI+tg3ddQaXNUQSTrcFbF2MDforFYLEpMSP6XfQWa0zOJ5ijHk/cjn0Bc80d9h2F256g3px8gpRq3M9U2nwMrXzIkyg8dR/V2ZOWJZilFGk9sZOH3v3QXkShRxqlZuUTvF9de+zU8pzTtSwm2LIWMruUJXifpt7ETpycfa/mZDcxD29yrA0jeF9N43N6h9bM71YdsePKcqwNI3gJpsVO7HJEGqQd0RU7blqONbldRZs+pVIqMh3PSPxgqw1oig1FKqTQpy1ftcQzQdoC/wULpAXPsp1f9hW1akHdKEcwCZarQ0t2v7IEr1xHiS2xuXRsFNmiBNe9ilIPZdOGCRM05GfTXAzVg+MT9KHI8dHrwdgVbXSMWdHGrsmjIVFNznYVZ2K6ijhMdyZJV0G2LzoV2RdFYxx90VidXRTG2dmN3puOxAR6Uyizf9zd9f7oTFwQQ1HkcwfHcT/4xvfJbwdDmOVQohvOoWyBHC8KLdKoWUfkHa1Ds0aLRv+3oGBMkgI1VvnMKvWmKUePdi2aXdXsH2H06f8CL6KT+5n69f0AAAAldEVYdGRhdGU6Y3JlYXRlADIwMjEtMDMtMDJUMDk6MTM6NDEtMDU6MDBR1NmyAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIxLTAzLTAyVDA5OjEzOjQxLTA1OjAwIIlhDgAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAASUVORK5CYII='
pausar = b'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAFWUlEQVRogc2aTWxUVRTHf/e+92ZaioJD+TLSugEDlpWkLgwxRBM3dGNgoSYuFYiJGEC2utKgYjTIR1y6MX5sSJcaFmywTUzkKwRYSDEEIgy0BdrOm3uPuW+m8JhOZ96daWv/k5d5M+/cc8//3HvPOfe9p/hshLah1QuUZAvdwVYmZAMT9kU0KwFVVS1YbtKhL7JEX6VYPo1mGLjcVteldbROQOhGyU6UegfhlcRUI45M43ZlAREINeTUEMuDH7gV/4hWtxeGgA160GYvsDfl4VZgEIKEdJSo+Rqjv0Hbaz4EtFfHkTqAEtfBR20a7xAkGkLlRtMdTuffaHvQR0k2AibehDV/EHMIZVs1OIM1FkzwOdoOE5iNmZo0legKdqLzF9BBf8VV8wwlYxi9BRNdpBzuaI+AyG7ul3+aV6/PxNMoJsFCWPoZZE8j4dkJPJx4H62Potqd6i2h47F56jt0aZcfga6nBujIH0/C3WKABMeQZQMzLJF/6xCIir2M3j+J9gtQ8woJQd8/ibnVk+6mwJ91CJjCIOEi8fwjuORnQK0eTP9bXLOihkBZDmBUHwsSbrxhUXozebv/UcOp5alMrHUBkTuLZt7XhbhKwH2tILBFjEqNgMin2HkPlzEwATyoHmOAq4HK2ZqrSrIL7CfJz0CqI9AVFhiN7xA4GZ+wOdtozabDV75h1wUUd8PkR2/ubc5MwdOBjwJH9jhw+omyGbYi7Jphk698c7yF5Wh1DdizlNRmch5aEoN4Hfi95sprCL/VJ+Ah37R/uYIpbdAY3YvWm4m86oXpufBsnWvT/6XntW0o30qy13o9OtejidQ2RsvOOz6Z614GmTh1/rAFExvD5YVcsE3TE/Y33UXNxGgGmVzq/MGcE3DuWRf1a66X+ujyWLwVmAwyaaVTvh00RaRhpNSniWVDC819C6X5yY6xrNdoVrXQ1HvI5gWaNXoO9rbto7XxcZFNLVTNnMVJLdUxukX+uQwytf00w1gLOkVj5ZZnQ4fODDJpj2Yh4OcUN6ZWbmoifaWFVZCFQDoTRxnkO7wscO7J6cuantx5xjJWs4+RxVvpqRlmNCk7Jg08l7+g+SceQpQbkizJyQdpAlnCrh+BDoEbk0OaSXuK5aFr7qeg+bRLE8iyBrKM0jQMKoIpe0oTcI2yOUdss8zTWtxo8F96RHXNtXry2UN6LAHYvyjHIxXWfUtPcGb8iHdwhHeB1TM2KBWMA0ur5/nq944aeYc3vINIYrU6QZSrbik7c88wPlX031JSP41U1pTb63bXl20j+Uu1ualsKSvDNlG6S04fqQ5iyU+jmnlU7OueXbYNKHHHtwTcdRv81G2VsICVO6hyxYOLFe62itUrCOMiJkotHFsuIpMHqhHPOzHMO0QeJOs8b/Ynxjt0lmtWvoq+ROQc4hXSFgJFyqoLWz5LzFeP+uu6WSd0yY3t6MVR7lfhnnAWCEOQ29vTFwo3b9choNaOIEsGkrWwGDBhFaFLKUsHCFZdT1tU5KXZksf4IGH8XhKySgv6dOZJuL473b3Q0i7UvcEZ19XKBtkv7vwerXeTV//PvWqZLhllD9J5YjaxJs/I7HF0x04k+SwcXBh3h8m7zH2sUb/N6w8z9QsytQnM0MLkB+3uPg8T2Y0E8a8ZpDMgyF9CBS+Tl4/dJm6OYR5XGNo57CBW9WPUpYx0PVDiCwT3nOrwHHCwyXsTEyZAJxQOg+4liA75KPF3p7YulO1DyUoUHwLnvXUkz7zQdKoz9OQ/wFj3Zss+pOz95sncvG6DrEepVxHeBJ4H1gLLaspsd/PgPMJVlDqNioeR8Epb3ZbW8R8fLcmt70JtLwAAAABJRU5ErkJggg=='

#layout

layout = [
    [sg.Text('STOPWATCH',size=(40,1),justification='center',font=('Directive Four Condensed',30),text_color='Blue')],
    [sg.Text('How many minutes?        '),sg.DropDown((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15),default_value=0,size=(5,16),key='listamin',background_color='Black',tooltip='minutos',pad=(4,6))],
    [sg.Text('How many seconds?       '),sg.DropDown((0,1,5,10,15,20,30,40,50,60),default_value=0,size=(5,16),key='seg',background_color='Black',tooltip='minutos',pad=(4,6))],
    [sg.Text('Turn on notifications?     '),sg.Checkbox('',key='noti',default=False,enable_events=True)],
    [sg.Text('A cada quantos minutos?'),sg.DropDown((1,2,3,5,10,15,20),default_value=1,disabled=True,key='noti2',background_color='black',size=(5,16))],
    [sg.Text('                 ',key='branco') ,sg.Button('',image_data=play,key='comecar',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0), sg.Button('',image_data=stop,border_width=0,button_color=(sg.theme_background_color(),sg.theme_background_color()),key='parar',visible=False),sg.Button('',key='pausar',visible=True,border_width=0, image_data=pausar,button_color=(sg.theme_background_color(),sg.theme_background_color()))],
    [sg.Text('00:00',size=(40,1),justification = 'center',key='update',font=('Bahnschrift SemiBold Condensed',60))],
    [sg.Text('',size=(40,1),justification='center',key='pause')],
    [sg.Text('   '),sg.ProgressBar(max_value=0,orientation='h',size=(20,20),bar_color=('White','Blue'),key='progresso',style='alt')]
]

#Janela

window = sg.Window('STOPWATCH',layout,size=(300,450),no_titlebar=False,grab_anywhere=True, icon=icone)

#loop
while True:
    eventos,valores = window.read()

    print(eventos,valores)
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'noti':
        if valores['noti'] == True:
            window['noti2'].update(disabled=False)
        if valores['noti'] == False:
            window['noti2'].update(disabled=True)
            valores['noti2'] = 0
    segmin = valores['listamin'] * 60
    final = int(segmin) + int(valores['seg'])
    timer = minutos = 0
    teste = 0

    # COMECAR A CONTAGEM

    if eventos == 'comecar':
        window['progresso'].UpdateBar(max=final,current_count=0)
        window['comecar'].update(visible=False)
        window['parar'].update(visible=True)
        window['pausar'].update(visible=True)
        while True:
            eventos, valores = window.read(timeout=1000,timeout_key='timeout')

            if eventos == None or eventos == sg.WIN_CLOSED:
                break
            if eventos == 'parar':
                window['comecar'].update(visible=True)
                window['parar'].update(image_data=stop)
                break
            if eventos == 'pausar':
                window['pausar'].update(disabled=True)
                window['parar'].update(image_data=play)
                window['pause'].update(value='PAUSED')
                eventos,valores = window.read(timeout=100000000000)
                if eventos == 'pausar':
                    pass
                if eventos == 'parar':
                    window['pause'].update(value='')
                    window['pausar'].update(visible=True)
                    window['pausar'].update(disabled=False)
                    window['parar'].update(image_data=stop)

            if valores['noti'] == True:
                window['noti2'].update(disabled=False)
            if valores['noti'] == False:
                window['noti2'].update(disabled=True)

            timer += 1
            teste += 1
            window['progresso'].UpdateBar(teste)
            if timer == 60:
                timer = 0
                minutos +=1
                if teste == 300:
                    pass
                else:
                    if valores['noti'] == True:
                        if valores['noti2'] == 1:
                            toaster.show_toast('RECADO', 'Se passaram 1 minuto', duration=5,
                                               icon_path='C:/sla bixo/cronometro.ico', threaded=True)
            valor = valores['noti2']
            if valores['noti'] == True:
                toasttest = (teste/60)/int(valores['noti2'])
                if toasttest.is_integer() == True:
                    if valores['noti'] == True:
                        toaster.show_toast(f'RECADO', f'Se passaram {valor} minuto', duration=5,
                                               icon_path='C:/sla bixo/cronometro.ico', threaded=True)
            window['update'].update(f'{minutos:02d}:{timer:02d}')
            print(f'{minutos}:{timer}')
            print(f'{eventos}')
            if teste == final:
                sg.popup('CONTAGEM TERMINADA', button_color=('White', 'Blue'),line_width=9,no_titlebar=True)
                break
        window['parar'].update(image_data=stop)
        window['parar'].update(visible=False)
        window['comecar'].update(visible=True)
window.close()