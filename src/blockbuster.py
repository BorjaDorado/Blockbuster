def capitalize_first_letter(df, column_name):
    df[column_name] = df[column_name].str.title()
    return df