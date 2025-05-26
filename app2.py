import os
import markdown
from xhtml2pdf import pisa

# Define directories
INPUT_DIR = "input"
OUTPUT_DIR = "output"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# HTML template with improved LaTeX-like styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            margin: 2.5cm;
        }
        body {
            font-family: "Arial", sans-serif;
            line-height: 1.5;
            font-size: 12pt;
            text-align: justify;
        }
        h1, h2, h3 {
            color: #222;
        }
        p, ul, ol {
            page-break-inside: avoid;
            margin: 1em 0;
        }
        pre, code {
            max-width: 100%;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            background-color: #f5f5f5;
            padding: 10px;
            border: 1px solid #ddd;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 1em;
            margin-bottom: 1em;
            page-break-inside: avoid;
        }
        tr, tbody {
            page-break-inside: avoid;
        }
        th, td {
            border: 1px solid #000;
            padding: 4px;
            text-align: left;
        }
    </style>
</head>
<body>
{content}
</body>
</html>
"""

def convert_html_to_pdf(html_content, output_path):
    """Convert HTML content to PDF and save to the specified path."""
    with open(output_path, "wb") as pdf_file:
        pisa.CreatePDF(src=html_content, dest=pdf_file)
        print(f"✔ PDF generated: {output_path}")

def process_markdown_files():
    """Process all Markdown files in the input directory and convert them to PDF."""
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.md', '.markdown')):
            md_path = os.path.join(INPUT_DIR, filename)
            base_name = os.path.splitext(filename)[0]
            pdf_path = os.path.join(OUTPUT_DIR, f"{base_name}.pdf")

            try:
                # Read Markdown file
                with open(md_path, 'r', encoding='utf-8') as md_file:
                    md_content = md_file.read()

                # Convert Markdown to HTML
                html_body = markdown.markdown(md_content, extensions=["extra", "smarty"])
                full_html = HTML_TEMPLATE.format(content=html_body)

                # Convert to PDF
                convert_html_to_pdf(full_html, pdf_path)
            except KeyError as e:
                print(f"Error processing {filename}: Invalid template key {e}. Check the Markdown content.")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    process_markdown_files()