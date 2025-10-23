# -----------------------------------------------------
# 📱 Instagram Automation using Instabot
# -----------------------------------------------------
# Author: MD Jiyauddin
# Description: This script automates Instagram tasks such as:
# login, follow/unfollow, send messages, upload photo,
# view followers/following, like and comment on posts.
# -----------------------------------------------------

# Importing Instabot library    ............................ isko pip install instabot kar ke install karo
from instabot import Bot
import time

# 1️⃣ Create a bot instance

bot = Bot()

# 2️⃣ Login into your Instagram account

bot.login(
    username="your_insta_username",   # <-- Replace with your username
    password="your_insta_password"    # <-- Replace with your password
)

print("\n✅ Logged in successfully!\n")

# 3️⃣ Follow a user          ...................................... jisko bhi follow karna hai uska username daalo 

user_to_follow = "example_user_id"  # Replace with the username you want to follow
bot.follow(user_to_follow)
print(f"👤 Followed: {user_to_follow}")

time.sleep(2)

# 4️⃣ Upload a photo

photo_path = "C:/Users/YourName/Desktop/image.jpg"  # Replace with your image path
caption = "✨ Just testing Instabot automation! #python #automation #instabot"
bot.upload_photo(photo_path, caption=caption)
print("📸 Photo uploaded successfully!")

time.sleep(2)

# 5️⃣ Send Direct Messages                ......................................... jisko bhi meassage karna hai uska username daalo like one id or more then one id accept hai 

message_text = "Hey! 👋 This is an automated message sent using Instabot 🤖"
recipients = ["friend_username1", "friend_username2"]
bot.send_message(message_text, recipients)
print("💬 Message sent to:", recipients)

time.sleep(2)

# 6️⃣ Unfollow a user                                ................................. jisko unfollow karna hai uska username daalo 

user_to_unfollow = "example_user_id"
bot.unfollow(user_to_unfollow)
print(f"🚫 Unfollowed: {user_to_unfollow}")

time.sleep(2)

# 7️⃣ Get followers list                    .............................. followers ki list nikalo yaha se

your_username = "your_insta_username"
followers = bot.get_user_followers(your_username)
print("\n👥 Your Followers List:")
for follower in followers:
    info = bot.get_user_info(follower)
    print(f" - {follower}: {info['username']} | Bio: {info.get('biography', 'N/A')}")
    time.sleep(1)

# 8️⃣ Get following list                ............................................ following ki list nikalo yaha se 

following_users = bot.get_user_following(your_username)
print("\n➡️ People You Follow:")
for following in following_users:
    info = bot.get_user_info(following)
    print(f" - {following}: {info['username']} | Bio: {info.get('biography', 'N/A')}")
    time.sleep(1)

# 9️⃣ Like a user's last post           ..................................... like or user last post cheak kar sakte ho yaha se 

target_user = "example_user_id"
user_posts = bot.get_user_medias(target_user, filtration=None)
if user_posts:
    bot.like(user_posts[0])
    print(f"❤️ Liked {target_user}'s recent post!")

# 🔟 Comment on a post                                     ................................ jo comment karna hai wo likh kar username de do 

if user_posts:
    bot.comment(user_posts[0], "🔥 Nice post! Keep it up! #BeastMindset")
    print(f"💬 Commented on {target_user}'s post!")

# ✅ Done
#
print("\n✨ Automation completed successfully! 🚀")
