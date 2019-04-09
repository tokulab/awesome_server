from PIL import Image, ImageFilter, ImageOps
import sys
import pyocr
import pyocr.builders

# base64をキャッチするとこを別ライブラリから記載

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print('no ocr tools.')
    sys.exit(1)

#
# tool = tools[0]
# pilimg = Image.open('./test_src/penki.jpg')
# # pilimg.convert('L')
# pilimg = ImageOps.invert(pilimg)
# pilimg.show()
# infer = tool.image_to_string(
#     pilimg,
#     lang='jpn',
#     builder=pyocr.builders.TextBuilder(tesseract_layout=6)
# )
#
# print(infer)

class Ocr():
    def __init__(self):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            raise Exception('no ocr tools!')
        self.tool = tools[0]
        self.config = self.__set_config('./config.yaml')

    def read_img(self, name, num=1):
        relative_head = './'
        src_folder = 'test_src/' if self.config['test_mode'] == True else 'src/'
        path = relative_head + src_folder
        if num == 1:
            self.img = [Image.open(path+name)]
        else:
            self.img = []
            for i in range(int(num)):
                self.img.append(Image.open(path+name))

    def img_effect(self, *args, show=False):
        effect_dict = {
            'gray': ImageOps.grayscale,
            'reverse_rgb': ImageOps.invert,
        }
        for eff in args:
            self.img = [effect_dict[eff](img) for img in self.img]
            sys.stdout.write(eff)
            if eff != args[-1]:
                sys.stdout.write(' -> ')
            else:
                sys.stdout.write('\n')
            sys.stdout.flush()
        if show == True:
            for img in self.img:
                img.show()


    def img_to_str(self, target=0, **kwargs):
        if len(self.img) == 0:
            raise Exception('not read img!')
        infer = self.tool.image_to_string(
            self.img[target],
            lang=kwargs['lang'],
            builder=pyocr.builders.TextBuilder(tesseract_layout=kwargs['tesseract_layout'])
        )
        return infer

    def __set_config(self, config_path):
        import yaml
        with open(config_path, 'r+') as conf:
            config = yaml.load(conf)
        return config