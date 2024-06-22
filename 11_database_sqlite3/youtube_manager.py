import sqlite3

con = sqlite3.connect("youtube_videos.db")
cursor = con.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
"""
)


def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        return json.dump(videos, file)


def list_videos():
    res = cursor.execute("SELECT * FROM videos")
    for row in res.fetchall():
        print(row)


def add_video(name, time):
    res = cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()
    print("Video added successfully")


def update_video(video_id, new_name, new_time):
    res = cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, video_id),
    )
    con.commit()
    print("Video updated successfully")


def delete_video(video_id):
    res = cursor.execute(
        "DELETE FROM videos WHERE id = ?",
        (video_id,),
    )
    con.commit()
    print("Video deleted successfully")


def main():
    while True:
        print("\n Youtube Manager with Database | Choose an option")
        print("1. List videos")
        print("2. Add a video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = int(input("Enter the video ID to update: "))
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = int(input("Enter the video ID to delete: "))
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid option")

    con.close()


if __name__ == "__main__":
    main()
