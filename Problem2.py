def library_borrowing_analysis():
    print("Welcome to the Library Book Borrowing Analysis!")
    print("Enter the records in the format: 'Book Title - Days Borrowed', one per line.")
    print("Type 'done' when finished.")

    borrowed_books = {}

    
    while True:
        record = input("Enter record: ").strip()
        if record.lower() == "done":
            break
        try:
            title, days = record.split(" - ")
            days = int(days)
            if title in borrowed_books:
                borrowed_books[title] += days  
            else:
                borrowed_books[title] = days
        except ValueError:
            print("Invalid input! Please use the format 'Book Title - Days Borrowed'.")

    if not borrowed_books:
        print("\nNo records were entered. Exiting the analysis.")
        return

    most_borrowed = max(borrowed_books.items(), key=lambda x: x[1])
    least_borrowed = min(borrowed_books.items(), key=lambda x: x[1])
    total_days = sum(borrowed_books.values())
    total_books = len(borrowed_books)
    average_days = total_days / total_books
    unique_titles = set(borrowed_books.keys())
    sorted_books = sorted(borrowed_books.items(), key=lambda x: x[1], reverse=True)
    
    print("\n--- Analysis Results ---")
    print(f"Most borrowed book: {most_borrowed[0]} ({most_borrowed[1]} days)")
    print(f"Least borrowed book: {least_borrowed[0]} ({least_borrowed[1]} days)")
    print(f"Average borrowing time: {average_days:.2f} days")
    print(f"Unique titles: {unique_titles}")
    print("Books sorted by borrowing duration (descending):")
    for title, days in sorted_books:
        print(f"{title}: {days} days")

if __name__ == "__main__":
    library_borrowing_analysis()
