Detecção de Objetos com YOLOv8

Este projeto aplica um pipeline completo de detecção de objetos utilizando a arquitetura YOLOv8 com imagens customizadas. Ele abrange a coleta, anotação, preparação dos dados, treinamento e inferência de um modelo de visão computacional para uma classe específica.

Estrutura do Projeto

yolo/
├── anotacoes/
│   └── YOLODataset/
│       ├── dataset.yaml
│       ├── images/
│       │   ├── train/
│       │   └── val/
│       └── labels/
│           ├── train/
│           └── val/
├── treino.py
├── predizer.py
└── venv/

Etapas do Projeto

Ambiente
Foi utilizado um ambiente virtual Python com as bibliotecas necessárias para anotação, conversão e treinamento. As principais dependências são: ultralytics, labelme e labelme2yolo.

Anotação
As imagens foram anotadas manualmente com o Labelme. Os arquivos de anotação no formato JSON foram armazenados em uma pasta dedicada.

Conversão
As anotações no formato Labelme foram convertidas para o formato YOLO utilizando a ferramenta labelme2yolo. O processo resultou nos diretórios images/, labels/ e no arquivo dataset.yaml exigido pelo YOLOv8.

Treinamento
O modelo utilizado foi o yolov8n.pt, conhecido por sua leveza e velocidade. O treinamento foi realizado com 20 épocas, imagem com dimensão 640x640 e CPU. O modelo final foi salvo automaticamente em runs/detect/.

Predição
As predições foram feitas com o modelo treinado, utilizando as imagens da pasta de validação. As saídas foram geradas com as detecções sobrepostas nas imagens originais, armazenadas em uma subpasta dentro de runs/detect/.

Observações Finais

Este repositório apresenta um pipeline funcional para detecção de objetos com YOLOv8 utilizando imagens próprias. A abordagem pode ser expandida facilmente para múltiplas classes, mais dados ou aplicação em vídeos.