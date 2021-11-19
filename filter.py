from PIL import Image
import numpy as np


class ConvertImage:
    """ Класс конвертирующий картинку в черно-белый пиксель-арт

        Тест значения шага
        >>> a = ConvertImage(np.array(Image.open('image.jpg')), 10, 50)
        >>> a.step
        5

        Тест значения шага
        >>> a = ConvertImage(np.array(Image.open('image.jpg')), 10, 5)
        >>> a.step
        51

        Тест размера блока
        >>> a = ConvertImage(np.array(Image.open('image.jpg')), 99, 10)
        >>> a.size
        99
    """
    def __init__(self, image, size, gradation):
        self.image = image
        self.size = size
        self.step = 255 // gradation

    def convert_image(self):
        """ Конвертирует картинку в пиксель-арт

        Тест размера полученной картинки
        >>> ConvertImage(np.array(Image.open('image.jpg')), 10, 50).convert_image().size
        (750, 750)
        >>> ConvertImage(np.array(Image.open('test_image2.png')), 10, 50).convert_image().size
        (1920, 1748)

        :return: черно-белый пиксель-арт
        """
        height = len(self.image)
        width = len(self.image[1])
        for i in range(0, height, self.size):
            for j in range(0, width, self.size):
                medium_brightness = self.get_medium_brightness(i, j)
                self.set_grayscale(medium_brightness, i, j)
        return Image.fromarray(self.image)

    def set_grayscale(self, medium_brightness, i, j):
        """Закрашивает блок пикселей одной градацией серого цвета

        :param medium_brightness: Среднее значение яркости
        :param i: Левая сторона блока
        :param j: Верхняя сторона блока
        """
        self.image[i:i + self.size, j:j + self.size] = int(medium_brightness // self.step) * self.step / 3

    def get_medium_brightness(self, i, j):
        """ Вычисляет среднее значение яркости блока

        Тест исходной картинки
        >>> ConvertImage(np.array(Image.open('image.jpg')), 10, 50).get_medium_brightness(1,1)
        55

        Тест черно-белой картинки
        >>> ConvertImage(np.array(Image.open('test_image1.jpg')), 10, 50).get_medium_brightness(1,1)
        757

        Тест полностью чёрной картинки
        >>> ConvertImage(np.array(Image.open('test_image2.png')), 10, 50).get_medium_brightness(1,1)
        0

        :param i: Левая сторона блока
        :param j: Верхняя сторона блока
        :return: Среднее значение яркости
        """
        return int((self.image[i:i + self.size, j:j + self.size].sum()) // self.size ** 2)


original_image = Image.open(input("Введите имя исходного изображения:"))
pixels = np.array(original_image)
block_size = int(input("Введите размер блока (целое положительное число):"))
grad = int(input('Введите количество оттенков (целое положительное число):'))
result = ConvertImage(pixels, block_size, grad).convert_image()
result.save((input("Введите имя изображения, в которое запишется результат:")))
