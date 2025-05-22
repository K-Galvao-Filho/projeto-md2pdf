import os
import markdown
from xhtml2pdf import pisa

# Caminhos
INPUT_DIR = "input"
OUTPUT_DIR = "output"

# Cria a pasta de saída, se não existir
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Template HTML com estilo LaTeX-like
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <style>
        @page {{
            margin: 2.5cm;
        }}
        body {{
            font-family: "Arial", sans-serif;
            line-height: 1.5;
            font-size: 12pt;
            text-align: justify;
        }}
        h1, h2, h3 {{
            color: #222;
        }}
        p, ul, ol {{
            page-break-inside: avoid;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 1em;
            margin-bottom: 1em;
            page-break-inside: avoid;
        }}
        tr, tbody {{
            page-break-inside: avoid;
        }}
        th, td {{
            border: 1px solid #000;
            padding: 4px;
            text-align: left;
        }}
    </style>
</head>
<body>
{content}
</body>
</html>
"""

# Função para converter HTML → PDF
def converter_html_para_pdf(html_string, output_path):
    with open(output_path, "wb") as output_file:
        pisa.CreatePDF(src=html_string, dest=output_file)
        print(f"✔ PDF gerado: {output_path}")

# Loop pelos arquivos da pasta input/
for nome_arquivo in os.listdir(INPUT_DIR):
    if nome_arquivo.lower().endswith(('.md', '.markdown')):
        caminho_md = os.path.join(INPUT_DIR, nome_arquivo)
        nome_base = os.path.splitext(nome_arquivo)[0]
        caminho_pdf = os.path.join(OUTPUT_DIR, f"{nome_base}.pdf")

        with open(caminho_md, 'r', encoding='utf-8') as f:
            markdown_texto = f.read()

        # Converte markdown → HTML
        html_corpo = markdown.markdown(markdown_texto, extensions=["extra", "smarty"])
        html_completo = HTML_TEMPLATE.format(content=html_corpo)

        # Converte para PDF
        converter_html_para_pdf(html_completo, caminho_pdf)
