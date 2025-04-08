# Calculadora

## Descrição
Trata-se de um projeto simples de uma calculadora desenvolvida em Python 3.12, com o objetivo de aprofundar os estudos relacionados à biblioteca PySide6.
Dessa forma, é possível que sejam observadas determinadas particularidades no código, como a adoção do padrão camel case. Tal escolha se deve ao fato de a biblioteca PySide6, utilizada na construção da interface gráfica, adotar esse padrão de nomenclatura de forma nativa.
Em virtude disso, optou-se por não seguir a convenção snake case, tradicionalmente empregada em projetos Python, a fim de preservar a consistência e evitar possíveis conflitos na leitura do código.

## Tecnologias Utilizadas
- Python 3.12
- PySide6 (Qt for Python)

## Estrutura do Projeto
```
├── dist/
│   └── Calculadora.exe     # Executável gerado
│
├── main.py                 # Ponto de entrada da aplicação
├── main_window.py          # Lógica da janela principal da interface gráfica
│
├── buttons.py              # Configuração e lógica dos botões
├── display.py              # Lógica e configuração do display numérico
├── info.py                 # Lógica e label informativo
├── style.py                # Estilo e aparência da interface com qss
│
├── util.py                 # Funções auxiliares e utilitárias
├── enviroments.py          # Variáveis e configurações
│
└── requirements.txt        # Lista de dependências do projeto
```

## Observação
- Este projeto possui fins didáticos e não tem a pretensão de ser uma calculadora completa.
