import re

def markdown_to_html(markdown_text):
    # Convert headers
    markdown_text = re.sub(r'(^#{1,6})\s*(.*$)', lambda match: f"<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>", markdown_text, flags=re.MULTILINE)
    
    # Convert horizontal rules
    markdown_text = re.sub(r'^---$', "<hr>", markdown_text, flags=re.MULTILINE)

    # Convert blockquotes
    markdown_text = re.sub(r'^>\s*(.*)$', r'<blockquote>\1</blockquote>', markdown_text, flags=re.MULTILINE)

    # Convert ordered lists
    markdown_text = re.sub(r'^(\d+\.)\s*(.*)$', r'<ol><li>\2</li></ol>', markdown_text, flags=re.MULTILINE)

    # Convert unordered lists
    markdown_text = re.sub(r'^-\s*(.*)$', r'<ul><li>\1</li></ul>', markdown_text, flags=re.MULTILINE)

    # Convert images
    markdown_text = re.sub(r'\!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', markdown_text)

    # Convert links
    markdown_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown_text)

    # Convert bold
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown_text)

    # Convert italic
    markdown_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', markdown_text)

    # Convert code
    markdown_text = re.sub(r'`(.*?)`', r'<code>\1</code>', markdown_text)

    return markdown_text

example = """
# Heading 1
## Heading 2
### Heading 3

*italicized text* and **bold text** and `code`

> blockquote

1. First item
2. Second item
3. Third item

- First item
- Second item
- Third item

---

[Pagina da Porsche](https://www.porsche.com)

![Porsche Carrera Gt](https://images-porsche.imgix.net/-/media/CBFCF1F74F414D3EB9BE27954BC570DC_0076C9CE80A34079B5CCC7E37564FD62_00X_Easy-Model-Selector_14_CL16H00IX0001_1_GL_5_175_rgb?w=1920&h=1080&q=45&crop=faces%2Centropy%2Cedges&auto=format)
"""

html_output = markdown_to_html(example)
with open("output.html", "w") as html_file:
    html_file.write(html_output)

print("HTML file created successfully!")
