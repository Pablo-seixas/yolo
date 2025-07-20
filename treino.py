from ultralytics import YOLO

# Caminho real do dataset.yaml
dataset_yaml = "/home/seixas/Documentos/yolo/anotacoes/YOLODataset/dataset.yaml"

# Carrega o modelo YOLOv8 nano (leve e rápido)
model = YOLO("yolov8n.pt")

# Inicia o treinamento
model.train(
    data=dataset_yaml,
    epochs=20,
    imgsz=640
)
