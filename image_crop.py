import math
from PIL import Image
from CTkMessagebox import CTkMessagebox

# Open the image
def foto_kirpma(foto_uzanti, foto_kaydetme_konumu, x1, y1, x2, y2):

    try:
        image = Image.open(foto_uzanti)
        def foto_kirpma2(x1_tam, y1_tam, x2_tam, y2_tam,foto_kaydetme_konumu,image):
            kirpilmis_resim = image.crop((x1_tam, y1_tam, x2_tam, y2_tam))
            kirpilmis_resim.save(foto_kaydetme_konumu)

        if x1 - x2 > 0 and y1 - y2 > 0:
            x1_tam = math.ceil(x2)
            y1_tam = math.ceil(y2)

            x2_tam = math.ceil(x1)
            y2_tam = math.ceil(y1)

            foto_kirpma2(x1_tam, y1_tam, x2_tam, y2_tam,foto_kaydetme_konumu,image)

        elif x1 - x2 < 0 and y1 - y2 > 0:
            x1_tam = math.ceil(x1)
            y1_tam = math.ceil(y2)

            x2_tam = math.ceil(x2)
            y2_tam = math.ceil(y1)

            foto_kirpma2(x1_tam, y1_tam, x2_tam, y2_tam,foto_kaydetme_konumu,image)

        elif x1 - x2 > 0 and y1 - y2 < 0:
            x1_tam = math.ceil(x2)
            y1_tam = math.ceil(y1)

            x2_tam = math.ceil(x1)
            y2_tam = math.ceil(y2)

            foto_kirpma2(x1_tam, y1_tam, x2_tam, y2_tam,foto_kaydetme_konumu,image)

        else:
            x1_tam = math.ceil(x1)
            y1_tam = math.ceil(y1)

            x2_tam = math.ceil(x2)
            y2_tam = math.ceil(y2)

            foto_kirpma2(x1_tam, y1_tam, x2_tam, y2_tam,foto_kaydetme_konumu,image)
    except:
        CTkMessagebox(title="Error", message="No Valid Folder or Photo Found!!!", icon="cancel",
                      width=400, height=200)
