def markdown_to_html(markdown_text):
    html_text = ""

    in_blockquote = False
    in_ordered_list = False
    in_unordered_list = False

    for line in markdown_text.split("\n"):
        
        # Cabecalhos
        if line.startswith("#"):
            level = line.count("#")
            html_text += f"<h{level}>{line[level+1:]}</h{level}>"

        # Linha horizontal
        elif line.strip() == "---":
            html_text += "<hr>"

        # Quotes
        elif line.startswith(">"):
            if not in_blockquote:
                html_text += "<blockquote>"
                in_blockquote = True
            html_text += line[1:].strip()
        elif in_blockquote:
            html_text += "</blockquote>"
            in_blockquote = False

        # Lista ordenaad
        elif line.strip() and line[0].isdigit() and line[1] == ".":
            if not in_ordered_list:
                html_text += "<ol>"
                in_ordered_list = True
            html_text += f"<li>{line.split('.', 1)[1].strip()}</li>"
        elif in_ordered_list:
            html_text += "</ol>"
            in_ordered_list = False

        # Lista não ordenada
        elif line.startswith("-"):
            if not in_unordered_list:
                html_text += "<ul>"
                in_unordered_list = True
            html_text += f"<li>{line[1:].strip()}</li>"
        elif in_unordered_list:
            html_text += "</ul>"
            in_unordered_list = False

        # Imagem
        elif "!" in line and "[" in line and "]" in line and "(" in line and ")" in line:
            start_alt = line.find("[")
            end_alt = line.find("]")
            start_src = line.find("(")
            end_src = line.find(")")
            if start_alt < end_alt and end_alt < start_src and start_src < end_src:
                alt = line[start_alt+1:end_alt]
                src = line[start_src+1:end_src]
                if alt:
                    html_text += f'<img src="{src}" alt="{alt}">'
                else:
                    html_text += f'<img src="{src}">'

        # Link
        elif "[" in line and "]" in line and "(" in line and ")" in line:
            start_link = line.find("[")
            end_link = line.find("]")
            start_url = line.find("(")
            end_url = line.find(")")
            if start_link < end_link and end_link < start_url and start_url < end_url:
                title = line[start_link+1:end_link]
                url = line[start_url+1:end_url]
                html_text += f'<a href="{url}">{title}</a>'

        # Texto com ou sem formatação
        else:
            inside_italic = False
            inside_bold = False
            inside_code = False
            current_word = ""

            i = 0
            while i < len(line):
                char = line[i]
                if char == "*":
                    if i + 1 < len(line) and line[i + 1] == "*":
                        if inside_bold:
                            html_text += f"<strong>{current_word}</strong>"
                            current_word = ""
                        else:
                            html_text += current_word
                            current_word = ""
                        inside_bold = not inside_bold
                        i += 1  
                    else:
                        if inside_italic:
                            html_text += f"<em>{current_word}</em>"
                            current_word = ""
                        else:
                            html_text += current_word
                            current_word = ""
                        inside_italic = not inside_italic
                elif char == "`":
                    if inside_code:
                        html_text += f"<code>{current_word}</code>"
                        current_word = ""
                    else:
                        html_text += current_word
                        current_word = ""
                    inside_code = not inside_code
                else:
                    current_word += char

                i += 1

    html_text += current_word + " "



    return html_text

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

print("Arquivo HTML criado com sucesso!")
