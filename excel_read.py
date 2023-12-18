import pandas as pd

def main():
    # 读取Excel文件
    excel_file_path = 'excel_file/file.xlsx'
    df = pd.read_excel(excel_file_path)

    # 输出第一行的数据
    first_row = df.iloc[1]
    print(first_row)

if __name__ == "__main__":
    main()
