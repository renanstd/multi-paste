# multi-paste

Com este pequeno app, feito por mim a pedido de um amigo, você pode configurar N textos, em diferentes slots, e colar o conteúdo deles usando os atalhos `ctrl + 1`, `ctrl + 2`, `ctrl + 3`, sucessivamente, em qualquer lugar do windows. Funciona como um "substituto" para o `ctrl + v`, porém com valores fixos.

![screenshot](https://github.com/renanstd/multi-paste/blob/main/screenshots/001.png)

## Stack

Neste mini projeto utilizei as seguintes libs:

- **keyboard**: Para detectar os atalhos de teclado, e manipular o mesmo para inserir os textos dos slots
- **pyperclip**: Para adicionar coisas ao `ctrl + v` do windows
- **auto-py-to-exe**: Para fazer o build
