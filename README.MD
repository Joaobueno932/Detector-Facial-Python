# Detecção de Rosto em Tempo Real – OpenCV e CVZone

## Visão Geral

Este projeto utiliza **OpenCV** e **CVZone** para capturar vídeo da câmera em tempo real e detectar rostos no fluxo de imagens.
O resultado é exibido em uma janela com os rostos destacados, permitindo acompanhar a detecção ao vivo.

## Funcionalidades

* Captura de vídeo da câmera padrão do sistema
* Detecção de rostos com `FaceDetector` do CVZone
* Exibição do vídeo com marcações nos rostos detectados
* Encerramento rápido pressionando a tecla `ESC`

## Pré-requisitos

* Python 3.x instalado
* Câmera conectada e funcionando

## Instalação das dependências

```bash
pip install opencv-python cvzone mediapipe
```

## Como Executar

1. Clone ou baixe o projeto.
2. Execute o script principal:

   ```bash
   python nome_do_arquivo.py
   ```
3. Uma janela chamada **"Resultado"** será aberta com o vídeo e as detecções.

## Notas

* É possível ajustar parâmetros de detecção no código, consultando a documentação do **CVZone**.
* O desempenho pode variar de acordo com a qualidade da câmera e da iluminação.

## Habilidades demonstradas

* Uso de **OpenCV** para captura e manipulação de vídeo
* Aplicação do **CVZone** para detecção de rostos
* Processamento de imagens em tempo real
* Integração com **MediaPipe** para visão computacional
