project title:TaskMaster
video demo:https://youtu.be/XBp-jM6iEUc
DESCRIPTION:
TaskMaster is a personal to-do list web-based application that I built for my final project for CS50x. The main idea behind this project was to create a simple, clean, and useful tool to help people manage their daily tasks efficiently.

It’s not just a basic to-do list — I wanted to make it feel like your own personal assistant, but in a lightweight form. The idea is to help users track their tasks, deadlines, and progress, all in one place, and at the same time give them a sense of satisfaction when they complete their work.

As a student myself, I know how difficult it is to stay organized, especially when there are too many things to remember. That’s why I thought a to-do web app with a login system, progress tracker, and priority tags would be a really useful project for me to build, and hopefully for others to use too.

⚙️ Features
Here’s a breakdown of what TaskMaster can do:

User Registration/Login:
Every user has to create their own account before using the app. I added this feature to keep each person’s tasks private and personal.

Adding Tasks:
After logging in, you can easily add tasks by entering the task name, picking a due date, and selecting a priority level (Low, Medium, High).

Deleting Tasks:
If you added a task by mistake or don’t need it anymore, you can delete it with a single click.

Progress Bar:
The app calculates how many tasks are completed vs. how many are remaining. The progress bar fills up as you complete your tasks. When it hits 100%, you know you’ve crushed your to-do list!

Priority Tags:
I used colored badges (like green for Low, orange for Medium, and red for High) to help users quickly recognize important tasks.

🗃️ Database Design
I used SQLite for the database since it’s lightweight and works perfectly with Flask for smaller apps like this one. I kept the design as simple as possible with two main tables:

users → Stores each user’s ID, username, and hashed password (using CS50’s built-in generate_password_hash() function).

todos → Stores each individual task, linked to the correct user via a foreign key relationship on user_id.

This makes sure that only you can see your own tasks, even though all users are using the same web app.

🎨 Design and User Interface
I tried to focus on simplicity first when designing the interface. I used Bootstrap to help with styling because I wanted to avoid wasting too much time hand-writing CSS, but I still customized some parts, like the priority badges and the progress bar, to make the experience more visually appealing.

I originally thought about adding things like dark mode and more advanced styling, but I decided to stick with focusing on the core functionality first. I’d rather have something that works well than something that just looks pretty but doesn’t function properly.

⚔️ Challenges Faced
Honestly, building TaskMaster wasn’t easy for me. I’ve followed all the CS50 lectures and problem sets, but this was my first time building something without any guides or walkthroughs. I spent a lot of time figuring out how to structure a Flask app properly, and things like managing user sessions were confusing at first.

Another hard part was working with HTML forms and getting data from the forms into the database. I had to test a lot to make sure tasks were saving correctly and that each task was linked to the right user.

Also, CSS is still pretty confusing for me, so I used ChatGPT’s help to guide me through making the layout not look completely plain.

💡 Why I Chose This Project
I chose to build a to-do web app because I wanted something that could be used daily by normal people — not just coders, not just students, but anyone who needs help organizing their tasks. I think having your own task manager online feels nice because it’s yours. Plus, I’ve always wanted to build something that could actually help someone, not just solve random coding puzzles.

Also, I wanted to really test myself by going beyond what the CS50 problem sets taught and doing something practical.

🚀 Future Plans
Even though this is a small project, I don’t want to stop here. In the future, I plan to:

Add Dark Mode for better accessibility

Add task editing (right now, you can only delete tasks)

Let users mark tasks as completed with a tick instead of deleting them

Maybe add categories or tags so users can organize their tasks better

Eventually, I’d love to deploy it online so others can use it too

🙏 Ending Thoughts
Overall, I’m really proud of completing this. CS50 wasn’t easy, but it taught me that I can build real things using what I learned. It’s not perfect, but it’s a real working app that I coded on my own, using Flask, HTML, CSS, SQL, and Python.

Thank you to Professor David Malan, the CS50 team, and everyone who helped make this course possible. It’s been a crazy ride, but I’m really grateful for what I’ve learned.
