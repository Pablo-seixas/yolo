from ultralytics import YOLO

# Caminho para o modelo treinado
model = YOLO("runs/detect/train3/weights/best.pt")

# Caminho para imagens onde você quer prever (use o seu dataset por enquanto)
results = model.predict(source="/home/seixas/Documentos/yolo/anotacoes/YOLODataset/images/val", save=True)

# (Opcional) Mostrar resultado resumido no terminal
for r in results:
    print(r.boxes)
