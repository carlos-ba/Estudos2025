from PyQt6 import QtWidgets
import sys

class MinhaJanela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Aplicação")
        self.setGeometry(100, 100, 800, 600)

        # Criar widgets
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Campo de texto
        self.campo_texto = QtWidgets.QLineEdit()
        self.campo_texto.setPlaceholderText("Digite algo aqui...")
        self.layout.addWidget(self.campo_texto)

        # Adicionar elementos
        self.botao = QtWidgets.QPushButton("Clique Aqui")
        self.botao.clicked.connect(self.botao_clicado)  # Conectar o botão à função
        self.layout.addWidget(self.botao)

        # Label para mostrar resultado
        self.label_resultado = QtWidgets.QLabel("")
        self.layout.addWidget(self.label_resultado)

    def botao_clicado(self):
        texto = self.campo_texto.text()
        if texto:
            self.label_resultado.setText(f"Você digitou: {texto}")
        else:
            self.label_resultado.setText("Por favor, digite algo no campo de texto!")


# Inicializar a aplicação
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec())