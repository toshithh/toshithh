def typing_svg(text, interval=0.12, spacing=-10):
    content = ""
    for i in range(len(text)):
        content += f'    <tspan dx="{0 if i == 0 else spacing}" opacity="0"><animate attributeName="opacity" begin="{i*interval}s" dur="0.01s" to="1" fill="freeze"/>{text[i] if text[i]!= " " else "&#160;"}</tspan>\n'

    svg = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="150">
  <text x="50" y="100" font-family="Fira Code, monospace" font-size="48px" fill="#39FF14">

    {content}

    <tspan dx="{spacing}" opacity="0" id="caret">
      |
      <animate attributeName="opacity" values="0;1;0" dur="0.5s" repeatCount="indefinite" begin="{len(text)*interval}s"/>
    </tspan>

  </text>
  <desc>Toshith's typing animation</desc>
</svg>
"""
    return(svg)

def save_to_file(file, text):
    file = open(file, 'w')
    file.write(text)
    file.close()

save_to_file("Toshith.svg", typing_svg(input("Text: ")))
