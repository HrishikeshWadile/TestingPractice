import pandas as pd


def count_students(df, threshold):
    try:
        if df.empty:
            raise ValueError("Excel file is empty")

        subjects = [col for col in df.columns if col.lower() != "name"]

        count = 0

        for _, row in df.iterrows():
            passed_subjects = [subj for subj in subjects if row[subj] > threshold]

            if passed_subjects:
                count += 1

        return count

    except Exception as e:
        print(f"Error: {str(e)}")
        return 0


def run_test_case(df, threshold, expected, test_name):
    print(f"\n{'='*60}")
    print(f"TEST CASE: {test_name}")
    print(f"Threshold: {threshold}")
    print(f"Expected Result: {expected}")

    actual = count_students(df, threshold)

    print(f"Actual Result: {actual}")

    if actual == expected:
        print("STATUS: PASS")
    else:
        print("STATUS: FAIL (Mismatch detected)")

    print(f"{'='*60}")


def main():
    try:
        df = pd.read_excel("student_records.xlsx")

        print("Student Data:")
        print(df)

        run_test_case(
            df=df,
            threshold=40,
            expected=7, 
            test_name="Students scoring > 40 (Expected mismatch)"
        )

        run_test_case(
            df=df,
            threshold=60,
            expected=4,
            test_name="Students scoring > 60 (Expected match)"
        )

    except FileNotFoundError:
        print("Excel file not found: student_records.xlsx")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()