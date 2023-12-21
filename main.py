from docx import Document
from excel_read import read_xlsx_file_and_return_replace_list

def replace_text_in_docx(source_file_path, replacements, save_file_path):
    doc = Document(source_file_path)

    for para in doc.paragraphs:
        for run in para.runs:
            for new_text, old_text in replacements:
                # 类型转换string
                old_text = str(old_text)
                new_text = str(new_text)
                if old_text in run.text:
                    run.text = run.text.replace(old_text, new_text)

    doc.save(save_file_path)

if __name__ == "__main__":
    source_file_path = "word_file/example.docx"
    source_excel_path = "excel_file/example.xlsx"
    replacements_list = read_xlsx_file_and_return_replace_list(source_excel_path)

    for i, replacements in enumerate(replacements_list):
        save_file_path = f"word_file/save_path/example_save{i}.docx"
        replace_text_in_docx(source_file_path, replacements, save_file_path)
