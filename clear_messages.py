import sqlite3

DB_NAME = "Messages.db"

def clear_messages():
    """Удаляет все сообщения из таблицы Messages"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Подсчет количества сообщений перед удалением
    cursor.execute("SELECT COUNT(*) FROM Messages")
    count_before = cursor.fetchone()[0]
    
    # Удаление всех сообщений
    cursor.execute("DELETE FROM Messages")
    conn.commit()
    
    print(f"Удалено сообщений: {count_before}")
    
    conn.close()

if __name__ == "__main__":
    clear_messages()
    print("Все сообщения успешно удалены!")
