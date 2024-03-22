import os

"""
    这个函数是删除项目的.txt .text文本，因为有些是行输入，会续写在文本中，而项目逻辑需要用到按行读取数据,后缀名不同是要区分每次计算的文本和结果文本
"""


class deleteFile:
    @staticmethod
    def delete_txt_files(folder_path):
        files = os.listdir(folder_path)
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(folder_path, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except OSError as e:
                    print(f"Error deleting {file_path}: {e}")

    @staticmethod
    def delete_text_files(f_p):
        files = os.listdir(f_p)
        for file in files:
            if file.endswith(".text"):
                file_path = os.path.join(f_p, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except OSError as e:
                    print(f"Error deleting {file_path}: {e}")


if __name__ == '__main__':
    df = deleteFile()
    df_path = 'E:\\pydemo\\Agent\\'
    df.delete_text_files(df_path)
    df.delete_txt_files(df_path)
