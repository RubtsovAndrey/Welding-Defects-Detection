import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from ultralytics import YOLO
import time

# Загрузка модели YOLO
# Load the YOLO model
model = YOLO('welding_v2_aug/train3/weights/best.pt')


def draw_predictions(image_path, output_path):

    image = Image.open(image_path)

    # Измерение времени выполнения предсказания
    # Measure the inference time
    start_time = time.time()
    results = model(image)
    end_time = time.time()

    # Рассчитываем время выполнения
    # Calculate the inference time
    inference_time = end_time - start_time

    detections = results[0].boxes.data
    draw = ImageDraw.Draw(image)

    # Установка параметров шрифта
    # Set font parameters
    try:
        font = ImageFont.truetype("arial.ttf", size=20)
    except IOError:
        font = ImageFont.load_default()

    if detections is not None and len(detections) > 0:
        class_description = {}

        for detection in detections:
            x1, y1, x2, y2 = map(int, detection[:4])
            confidence = detection[4].item()
            class_id = int(detection[5])
            class_name = model.names[class_id]

            # Установка цвета и текста на основе класса
            # Set color and text based on class
            if class_name == 'good weld':
                color = 'green'
                label_text = f'Хороший шов ({confidence:.2f})'
            elif class_name == 'bad weld':
                color = 'red'
                label_text = f'Плохой шов ({confidence:.2f})'
            elif class_name == 'defect':
                color = 'orange'
                label_text = f'Дефект ({confidence:.2f})'
            else:
                color = 'blue'
                label_text = f'Неизвестный ({confidence:.2f})'

            # Отрисовка прямоугольника и текста
            # Draw rectangle and text
            draw.rectangle([(x1, y1), (x2, y2)], outline=color, width=5)

            # Получаем размеры текста и рисуем фон для текста
            # Get text size and draw background for text
            text_bbox = draw.textbbox((x1, y1), label_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            draw.rectangle([(x1, y1 - text_height - 10), (x1 + text_width, y1)], fill=color)
            draw.text((x1, y1 - text_height - 10), label_text, fill="white", font=font)

            # Добавление текстового описания для вывода
            # Add textual description for output
            if label_text not in class_description:
                class_description[label_text] = label_text

    # Добавление информации о времени выполнения
    # Add inference time information
    draw.text((10, image.height - 30), f'Время выполнения: {inference_time:.2f} сек', fill='white', font=font)

    plt.figure(figsize=(10, 10))  # Увеличиваем размер отображаемого изображения
    # Increase the figure size
    plt.imshow(image)
    plt.title('Sample Predictions')
    plt.axis('off')
    plt.savefig(output_path)
    plt.show()


# Пути к изображениям
# Paths to images
good_weld_image_path = 'visualization/1660831012017.jpeg'
bad_weld_image_path = 'visualization/bad_weld.jpg'

# Выполнение визуализации для хорошей сварки
# Performing visualization for good weld
draw_predictions(good_weld_image_path, 'visualization/sample_predictions_good_weld.png')

# Выполнение визуализации для плохой сварки
# Performing visualization for bad weld
draw_predictions(bad_weld_image_path, 'visualization/sample_predictions_bad_weld.png')
