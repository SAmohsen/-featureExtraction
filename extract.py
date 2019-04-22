import cv2
import matplotlib.pyplot as plt
number_of_sub_regions = 4


def show_char(img_list):
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    axs[0, 0].imshow(img_list[0])
    axs[0, 1].imshow(img_list[1])
    axs[1, 0].imshow(img_list[2])
    axs[1, 1].imshow(img_list[3])
    plt.show()


def get_sum_of_pixels(img):
    total_sum = 0
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            total_sum += img[row][col]
    return total_sum


def divide_img(img):
    rows = img.shape[0]
    cols = img.shape[1]
    divide_row = int(rows/2)
    divide_col = int(cols/2)
    img1 = img[:divide_row, :divide_col]
    img2 = img[:divide_row, divide_col:]
    img3 = img[divide_row:, :divide_col]
    img4 = img[divide_row:, divide_col:]
    # show_char([img1, img2, img3, img4])
    return [img1, img2, img3, img4]


def extract(img_src_file):
    # 10 features
    feature_vect = []
    sum_vect = []
    char_img = cv2.imread(img_src_file, 0)
    pxls_sum = get_sum_of_pixels(char_img)
    imgs = divide_img(char_img)
    for img in imgs:
        sum_vect.append(get_sum_of_pixels(img))
    for i in range(number_of_sub_regions):
        feature_vect.append(sum_vect[i] / pxls_sum)
    return feature_vect


'''
# driver code 
if __name__ == '__main__':
    features = extract('path /to /image/')

'''
