from xml.dom import minidom

file_path = 'word_file/example_zip/word/styles.xml'
dom = minidom.parse(file_path)

# 获取<w:styles>元素
styles_element = dom.getElementsByTagName('w:styles')
if styles_element:
    styles_element = styles_element[0]

    # 获取<w:rFonts>元素
    r_fonts_element = styles_element.getElementsByTagName('w:rFonts')
    if r_fonts_element:
        r_fonts_element = r_fonts_element[0]

        # 输出属性值
        print("Attribute: w:ascii =", r_fonts_element.getAttribute('w:ascii'))
        print("Attribute: w:eastAsia =", r_fonts_element.getAttribute('w:eastAsia'))
        print("Attribute: w:hAnsi =", r_fonts_element.getAttribute('w:hAnsi'))
        print("Attribute: w:cs =", r_fonts_element.getAttribute('w:cs'))
    else:
        print("w:rFonts element not found")
else:
    print("w:styles element not found")
