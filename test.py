from docx import Document

def replace_text_in_docx(file_path, replacements):
    """
    Replace text in a DOCX file while preserving the format.

    :param file_path: Path to the .docx file
    :param replacements: Dictionary of text replacements { "old_word": "new_word" }
    """
    doc = Document(file_path)
    
    for para in doc.paragraphs:
        for run in para.runs:
            for old_text, new_text in replacements.items():
                if old_text in run.text:
                    run.text = run.text.replace(old_text, new_text)
    
    doc.save(file_path.replace('.docx', '_modified.docx'))

# Specify the file path and replacements here
file_path = 'sue.docx'
replacements = {
    "xxx": "陈瑶",
    "dianhuahao": "17501240139",
    # Add more replacements as needed
}

replace_text_in_docx(file_path, replacements)

