from pptx_tools import utils


def get_ppt_img(filePath, png_folder):
    utils.save_pptx_as_png(png_folder, filePath, overwrite_folder=True)
    return True


if __name__ == '__main__':
    get_ppt_img(r'E:\Codes\AutoPlayer\data\samples.pptx', r'E:\Codes\AutoPlayer\data\ppt_img')
