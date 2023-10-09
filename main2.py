import streamlit as st
import pandas as pd

# Function to check if a guess is correct or approximate
def check_guess(df, guess):
    # Assuming the number is in the 'Number' column
    df["Difference"] = abs(df["Number"] - guess)
    closest_rows_10 = df[df["Difference"] <= 10]

    if not closest_rows_10.empty:
        # Display all matching users and the guessed number within 10
        result = f"Close! You are within 10 of the correct number ({guess}) for:\n"
        for _, row in closest_rows_10.iterrows():
            result += f"- {row['Name']} (Actual Number: {row['Number']})\n"
        return result
    else:
        # If no one is within 10, check within 20
        closest_rows_20 = df[df["Difference"] <= 20]
        if not closest_rows_20.empty:
            # Display all matching users within 20
            result = f"Close! You are within 20 of the correct number ({guess}) for:\n"
            for _, row in closest_rows_20.iterrows():
                result += f"- {row['Name']} (Actual Number: {row['Number']})\n"
            return result
        else:
            return "Sorry, try again. Your guess is not correct."

# Streamlit app
def main():
    st.title("Number Guessing Game")

    # Upload Excel file
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        # Read Excel file
        try:
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        except Exception as e:
            st.error(f"Error reading the file: {e}")
            return

        st.success("File uploaded successfully!")

        # Display the sheet content
        st.write("Sheet Content:")
        st.write(df)

        # Input guess number
        guess = st.number_input("Enter your guess:")

        # Check the guess
        if st.button("Check Guess"):
            if "Number" not in df.columns or "Name" not in df.columns:
                st.warning("The sheet does not contain both 'Number' and 'Name' columns.")
            else:
                result = check_guess(df, guess)
                st.write(result)

if __name__ == "__main__":
    main()
