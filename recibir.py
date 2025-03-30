import pandas as pd

def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)
    result = pd.concat([df_excel, df], ignore_index=True)
    result.to_excel(excel_path, index=False)

df = pd.DataFrame({"a":[11,22,33], "b":[55,66,77]})
append_df_to_excel(df, r"datos.xlsx")
