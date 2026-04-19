import pandas as pd

df = pd.read_excel("student_records.xlsx")

print(df.head())  

def update_value(df, lookup_head, lookup_value, change_head, change_value):
    try:

        if df[df[lookup_head] == lookup_value].empty:
            raise ValueError("Value not found")
        
        old_value = df.loc[df[lookup_head] == lookup_value, change_head].values[0]
        print(f"Old Value: {lookup_value} -> {old_value}")

        df.loc[df[lookup_head] == lookup_value, change_head] = change_value

        updated = df.loc[df[lookup_head] == lookup_value, change_head].values[0]
        assert updated == change_value

        print(f"Update Passed: {lookup_value} -> {change_value}")

    except Exception as e:
        print(f"Update Failed for {lookup_value}: {str(e)}")

update_value(df, "Name", "Aarav Sharma", "Marks", 87)
update_value(df, "Name", "Deepa Singh", "Marks", 75)
update_value(df, "Name", "Rahul", "Marks", 100) 

df.to_excel("student_records.xlsx", index=False)