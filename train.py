from ultralytics import YOLO


def train_model(data_config, epochs, img_size, batch_size, experiment_name, device):
    model = YOLO('yolov8m.pt')
    model.train(
        data=data_config,
        epochs=epochs,
        imgsz=img_size,
        batch=batch_size,
        device=device,
        save=True,
        project=experiment_name,
        name=experiment_name,
        lr0=0.01,
        momentum=0.937,
        weight_decay=0.0005,
        warmup_epochs=3.0,
        warmup_momentum=0.8,
        warmup_bias_lr=0.1,
        box=0.05,
        cls=0.5,
        iou=0.2,
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        translate=0.1,
        scale=0.5,
        mosaic=1.0,
        mixup=0.5,
        save_dir=f'runs/train/{experiment_name}'
    )


if __name__ == '__main__':
    DATA_CONFIG_PATH = 'data/The Welding Defect Dataset - v2/data.yaml'
    EPOCHS = 100
    IMG_SIZE = 640
    BATCH_SIZE = 16
    EXPERIMENT_NAME = 'welding_v2_aug'
    DEVICE = 'cuda'

    train_model(DATA_CONFIG_PATH, EPOCHS, IMG_SIZE, BATCH_SIZE, EXPERIMENT_NAME, DEVICE)
