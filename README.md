# Welding Defect Detection

## Description
This project is a demonstration application showcasing skills in machine learning tasks. It uses the YOLO model for weld defect detection and demonstrates image processing capabilities with machine learning technologies.

Этот проект является демонстрационным приложением, показывающим навыки работы с задачами машинного обучения. Он использует модель YOLO для обнаружения дефектов сварки и демонстрирует возможности обработки изображений с помощью технологий машинного обучения.

## Goals
1. **Develop a machine learning model for welding defect detection:** Train and deploy a YOLO-based object detection model to identify and classify welding defects.
2. **Demonstrate image processing capabilities:** Show how machine learning models can be used to annotate and analyze images of welds.
3. **Provide an easy-to-use tool for weld quality assessment:** Create a user-friendly interface to visualize model predictions and assess welding quality.

1. **Разработать модель машинного обучения для обнаружения дефектов сварки:** Обучить и развернуть модель детекции объектов на основе YOLO для идентификации и классификации дефектов сварки.
2. **Демонстрировать возможности обработки изображений:** Показать, как модели машинного обучения могут использоваться для аннотации и анализа изображений сварочных швов.
3. **Предоставить удобный инструмент для оценки качества сварки:** Создать удобный интерфейс для визуализации предсказаний модели и оценки качества сварки.

## Dataset
The model was trained using a welding defect dataset available on Kaggle. The dataset contains images of welds with annotations that classify the welds into different defect types. Dataset link: [Welding Defect Object Detection Dataset](https://www.kaggle.com/datasets/sukmaadhiwijaya/welding-defect-object-detection).

Модель была обучена с использованием датасета дефектов сварки, доступного на Kaggle. Датасет содержит изображения сварочных швов с аннотациями, которые классифицируют швы по различным типам дефектов. Ссылка на датасет: [Welding Defect Object Detection Dataset](https://www.kaggle.com/datasets/sukmaadhiwijaya/welding-defect-object-detection).

### Dataset Description
- **Images:** Contains images of welding seams with various types of defects annotated.
- **Annotations:** Objects are annotated with bounding boxes, indicating the defect class (e.g., "good weld", "bad weld", "defect").
- **Usage:** Used for training and evaluating object detection models such as YOLO.

### Описание датасета
- **Изображения:** Содержит изображения сварочных швов с аннотированными различными типами дефектов.
- **Аннотации:** Объекты аннотированы прямоугольными рамками, указывающими класс дефекта (например, "хороший шов", "плохой шов", "дефект").
- **Использование:** Используется для обучения и оценки моделей детекции объектов, таких как YOLO.

## Example Image Processing

Below are examples of image processing using the YOLO model:

**Example of a bad weld:**

![Bad Weld Example](visualization/sample_predictions_bad_weld.png)

**Example of a good weld:**

![Good Weld Example](visualization/sample_predictions_good_weld.png)

Ниже приведены примеры обработки изображений с использованием модели YOLO:

**Пример плохого шва:**

![Пример плохого шва](visualization/sample_predictions_bad_weld.png)

**Пример хорошего шва:**

![Пример хорошего шва](visualization/sample_predictions_good_weld.png)

## Results
- **Accurate Defect Detection:** The YOLO model effectively identifies and classifies welding defects with high accuracy.
- **Efficient Processing:** The model performs inference quickly, providing real-time feedback for weld quality assessment.
- **User-Friendly Visualization:** The results are displayed in an intuitive format, making it easy to understand the model's predictions.

- **Точная детекция дефектов:** Модель YOLO эффективно идентифицирует и классифицирует дефекты сварки с высокой точностью.
- **Эффективная обработка:** Модель выполняет инференс быстро, предоставляя обратную связь в реальном времени для оценки качества сварки.
- **Удобная визуализация:** Результаты отображаются в интуитивно понятном формате, что упрощает понимание предсказаний модели.

## Conclusion
This project serves as a practical demonstration of machine learning skills applied to welding defect detection. Although it is an educational project, the model can be practically applied, such as integrating it into a Telegram bot for real-time weld quality assessment.

Этот проект служит практической демонстрацией навыков машинного обучения, применённых к обнаружению дефектов сварки. Хотя это учебный проект, модель может быть практически применена, например, интегрирована в Telegram-бота для оценки качества сварки в реальном времени.
