#users user_id serial -> int 
CREATE_TABLE = {
    "users": """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            chat_id INT,
            state BOOLEAN,
            last_visit DATE
        );""",

    "books": """
        CREATE TABLE IF NOT EXISTS books (
            book_id SERIAL PRIMARY KEY,
            book_name VARCHAR(100) NOT NULL,
            author_name VARCHAR(30),
            book_info TEXT
        );""",

    "user_book": """
        CREATE TABLE IF NOT EXISTS user_book (
            user_book_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            book_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users (user_id),
            FOREIGN KEY(book_id) REFERENCES books (book_id)
        );""",

        
    "reviews": """
        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            title_review VARCHAR(100),
            review_text TEXT, 
            score INT CHECK(score >= 0 AND score <= 10), 
            user_id INT NOT NULL,
            book_id INT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (user_id),
            FOREIGN KEY (book_id) REFERENCES books (book_id)
        );""",
        
    "notes": """
        CREATE TABLE IF NOT EXISTS notes (
            note_id SERIAL PRIMARY KEY,
            note_text TEXT,
            note_number INT,
            note_date DATE,
            user_id INT NOT NULL,
            book_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users (user_id),
            FOREIGN KEY(book_id) REFERENCES books (book_id)
        );""",

    "active_list": """
        CREATE TABLE IF NOT EXISTS active_list (
            user_book_id SERIAL PRIMARY KEY,
            started_reading DATE,
            user_id INT NOT NULL,
            book_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users (user_id),
            FOREIGN KEY(book_id) REFERENCES books (book_id)
        );"""
}

