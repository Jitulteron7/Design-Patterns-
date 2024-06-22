class BitMap:
    def __init__(self, filename):
        self.filename = filename 
        print(f'Loading image from {filename}')
    
    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitMap:
    def __init__(self, filename):
        self.filename = filename
        self.bitmap = None 
    
    def draw(self):
        if not self.bitmap:
            self.bitmap = BitMap(self.filename)
        self.bitmap.draw()
        
        
def draw_image(image):
    print('about to print image')
    image.draw()
    print('done drawing image')


if __name__ == "__main__":
    # bmp = BitMap('facepalm.jpg')
    # draw_image(bmp)
    
    bmp = LazyBitMap('facepalm.jpg')
    draw_image(bmp)
    
    
    