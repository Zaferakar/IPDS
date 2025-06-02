import customtkinter as tk
import PIL
from PIL import Image, ImageTk
import customtkinter
import re


def koordinat_isaretleme(path,klasor_deger):#image location, location to save
    foto_kirpma = customtkinter.CTkToplevel()
    foto_kirpma.attributes("-topmost",True)
    global rect_id
    global x_katsayi, y_katsayi, wid_degismeyen, hgt_degismeyen
    img = PIL.Image.open(path)
    wid, hgt = img.size
    wid_degismeyen, hgt_degismeyen = img.size
    x_katsayi = wid / 1500
    y_katsayi = hgt / 1500
    oran = wid / hgt
    if hgt > wid:
        hgt = 1500
        wid = int(1500 * oran)
    elif hgt == wid:
        hgt = 1500
        wid = 1500
    else:
        hgt = int(1500 * oran)
        wid = 1500
    # specify frame size according to image
    WIDTH, HEIGHT = 1500, 1500
    topx, topy, botx, boty = 0, 0, 0, 0
    rect_id = None
    image = Image.open(path)
    def get_mouse_posn(event):
        global topy, topx
        topx, topy = event.x, event.y
    konum_liste = []
    def update_sel_rect(event):
        alt_liste = []
        global topy, topx, botx, boty
        botx, boty = event.x, event.y
        canvas.coords(rect_id, topx, topy, botx, boty)
        alt_liste.append(topx * x_katsayi * (1500 / wid))
        alt_liste.append(topy * y_katsayi * (1500 / hgt))
        if botx * x_katsayi * (1500 / wid) > wid_degismeyen:
            alt_liste.append(wid_degismeyen)
        elif botx * x_katsayi * (1500 / wid) < 0:
            alt_liste.append(0)
        else:
            alt_liste.append(botx * x_katsayi * (1500 / wid))
        if boty * y_katsayi * (1500 / hgt) > hgt_degismeyen:
            alt_liste.append(hgt_degismeyen)
        elif boty * y_katsayi * (1500 / hgt) < 0:
            alt_liste.append(0)
        else:
            alt_liste.append(boty * y_katsayi * (1500 / hgt))
        # limit if area larger than image size is selected
        konum_liste.append(alt_liste)
    foto_kirpma.title("Photo Crop Tool")
    foto_kirpma.geometry('%sx%s' % (WIDTH, HEIGHT))
    foto_kirpma.configure(background='grey')
    resize_image = image.resize((wid, hgt))
    img = ImageTk.PhotoImage(resize_image)
    canvas = tk.CTkCanvas(foto_kirpma, width=img.width(), height=img.height(),
                          borderwidth=0, highlightthickness=0)
    canvas.pack(expand=True)
    canvas.img = img
    canvas.create_image(0, 0, image=img, anchor=tk.NW)
    rect_id = canvas.create_rectangle(topx, topy, topx, topy,
                                      dash=(2, 2), fill='', outline='white')
    canvas.bind('<Button-1>', get_mouse_posn)
    canvas.bind('<B1-Motion>', update_sel_rect)
    foto_kirpma.wait_window()
    # konum liste[-1] = x1,y1,x2,y2


    try:
        from image_crop import foto_kirpma
        dosya_ismi_parcali = re.split(r"/", path)
         #update klasor_degeri

        foto_kirpma(path,klasor_deger+"/"+dosya_ismi_parcali[-1],konum_liste[-1][0],konum_liste[-1][1],konum_liste[-1][2],konum_liste[-1][3])
        return path,konum_liste[-1]

    except IndexError:
        dosya_ismi_parcali = re.split(r"/", path)
        foto_kirpma(path, klasor_deger + "/" + dosya_ismi_parcali[-1],0,0,wid_degismeyen, hgt_degismeyen )
        return path, [0,0,wid_degismeyen, hgt_degismeyen]





