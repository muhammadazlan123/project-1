import streamlit as st

# Library Management System

# Number of books in the library
total_books = 10  # Total books in the library
available_books = total_books  # Books currently available for borrowing
borrowed_books = 0  # Books currently borrowed
max_borrow_limit = 5  # Max books a user can borrow

# Streamlit UI
st.title("Personal Library Manager")

# Main options
menu = ["View available books", "Borrow a book", "Return a book", "Exit"]
choice = st.radio("Select an action", menu)

# Display the library status
if choice == "View available books":
    st.write(f"**Total books in library**: {total_books}")
    st.write(f"**Books available for borrowing**: {available_books}")
    st.write(f"**Books currently borrowed**: {borrowed_books}")

# Borrow a book
elif choice == "Borrow a book":
    if available_books > 0:
        if borrowed_books < max_borrow_limit:
            # Borrowing logic
            borrowed_books += 1
            available_books -= 1
            st.success("Book borrowed successfully!")
        else:
            st.warning("You have reached your borrow limit!")
    else:
        st.warning("No books are available for borrowing at the moment.")

# Return a book
elif choice == "Return a book":
    if borrowed_books > 0:
        borrowed_books -= 1
        available_books += 1
        st.success("Book returned successfully!")
    else:
        st.warning("You have no borrowed books to return.")

# Exit option
elif choice == "Exit":
    st.write("Exiting the system...")

