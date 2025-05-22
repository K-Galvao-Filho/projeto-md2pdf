# Conversor Markdown para PDF (com xhtml2pdf)

Este projeto converte automaticamente todos os arquivos `.md` ou `.markdown` contidos na pasta `input/` para arquivos PDF formatados profissionalmente, que serão salvos na pasta `output/`.

## ✅ Funcionalidades

- Conversão automática de múltiplos arquivos Markdown para PDF.
- PDFs gerados com **fonte Arial**, corpo justificado e espaçamento de 1,5.
- **Tabelas com bordas (`1px solid #000`)** e alinhamento correto.
- Prevenção de quebras de página em tabelas, parágrafos e listas.
- Compatível com Windows, Linux e macOS.

## 📦 Requisitos

Você precisa de Python 3.7+ e das seguintes bibliotecas:

```bash
pip install markdown xhtml2pdf
```

## 📁 Estrutura de Pastas

```
projeto-md2pdf/
├── app.py              # Script principal
├── input/              # Coloque aqui seus arquivos .md
│   └── exemplo.md
├── output/             # PDFs gerados serão salvos aqui
└── README.md           # Este arquivo
```

## ▶️ Como usar

1. Coloque seus arquivos `.md` ou `.markdown` na pasta `input/`.
2. Execute o script Python:

```bash
python app.py
```

3. Verifique a pasta `output/`. Para cada Markdown, será gerado um PDF com o mesmo nome.

## 📝 Exemplo de Markdown suportado

```markdown
# Relatório

Este é um exemplo de Markdown convertido para PDF.

## Tabela de Dados

| Nome     | Nota |
|----------|------|
| João     | 8.5  |
| Maria    | 9.0  |
| Roberto  | 7.5  |

## Lista

- Item 1
- Item 2
- Item 3
```

## ⚠️ Observações

- `xhtml2pdf` tem suporte limitado a CSS avançado (sem `flexbox`, `grid`, etc.).
- Para conteúdos mais complexos ou com muitas páginas, considere usar `WeasyPrint`.

## 📃 Licença

Projeto de uso livre para fins acadêmicos e profissionais.
