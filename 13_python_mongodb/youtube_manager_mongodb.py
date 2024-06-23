import pymongo
from bson import ObjectId

# from pymongo import MongoClient

client = pymongo.MongoClient(
    "mongodb://localhost:27017/", tlsAllowInvalidCertificates=True
)

db = client["VideoManager"]

video_collection = db["videos"]


def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {"_id": ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}}
    )
    print("Video updated successfully")


def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})
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
            video_id = input("Enter the video ID to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
