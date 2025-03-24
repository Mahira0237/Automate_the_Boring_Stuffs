from PIL import Image, ImageDraw, ImageFont
import os
textFile=open('I:\\My Drive\\AutomateTheBoringStuffs\\Chapter19\\CustomSittingCardsProject\\guests.txt','r')
names=textFile.readlines()
for i in range(0,len(names)):
    im = Image.new('RGBA', (288,360), 'white')
    draw = ImageDraw.Draw(im)
    draw.line([(0, 0), (287, 0), (287, 359), (0, 359), (0, 0)], fill='black')

    fontsFolder = 'C:\\Windows\\Fonts' # e.g. ‘/Library/Fonts'
    LucidaFont = ImageFont.truetype(os.path.join(fontsFolder, 'lhandw.ttf'), 10)
    arialFontName = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 20)
    arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 16)

    draw.text((10, 25), 'It would be a pleasure to have the company of',font=LucidaFont,fill='black')
    draw.text((100, 48), names[i].replace('\n',''), font=arialFontName,fill='black')
    draw.text((25, 80), 'at 1010 Memory Lane on the evening of',font=LucidaFont,fill='black')
    draw.text((120,95),'April 1st',font=arialFont,fill='black')
    draw.text((120,117),'at 7o\'clock',font=LucidaFont,fill='black')

    im.save(str(names[i].replace('\n',''))+'.png')

    FlowerIm = Image.open('Flower.png')
    FlowerIm=FlowerIm.resize((150,150))
    FlowerIm = FlowerIm.copy()
    im.paste(FlowerIm, (80, 200),FlowerIm)   

    im.save(str(names[i].replace('\n',''))+'.png')
