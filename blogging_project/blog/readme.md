**🚀 Detailed Explanation of the Blog & Comments System Project**
* This project is a mini-blogging system where users can:

1. Write blog posts
2. Tag posts with categories
3. Comment on posts
4. View analytics and trends using Django ORM queries

`📌 Key Learning Concepts in This Project :`
1. Django Models: Relationships (OneToOneField, ForeignKey, ManyToManyField)
2. Django ORM Queries: annotate(), aggregate(), Q objects, F expressions, select_related(), prefetch_related()
3. Django Views & Templates: Fetching data dynamically and displaying it in a frontend template
4. Django Template Language (DTL): Looping over querysets and displaying data dynamically.

# ------------------------------------------------------------------------------------------------------------------

1️⃣ **Database Models & Explanation :**
🟢 **1. User Model (Default Django User Model)**
`Django provides a built-in User model, which we’ll use for authentication. Each user can create multiple posts.`

🟠 **2. Profile Model (One-to-One Relationship with User)**
`Each User will have one Profile to store additional details like a bio and profile picture.`

🔵 **3. Post Model (One-to-Many with User, Many-to-Many with Tags)**
`A blog post belongs to one author, but can have multiple tags.`

🔹 ForeignKey(User, on_delete=models.CASCADE, related_name='posts'): Allows each post to be linked to a user.
🔹 ManyToManyField("Tag", blank=True, related_name="posts"): A post can have multiple tags.
🔹 views = models.PositiveIntegerField(default=0): Tracks how many times a post is viewed.

🟣 **4. Tag Model (Many-to-Many with Post)**
`Tags help categorize posts.`
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

🔹 ManyToManyField(Post): A tag can be attached to multiple posts.

🟡 **5. Comment Model (One-to-Many with Post)**
`A comment belongs to a single post and has an author.`
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

🔹 ForeignKey(Post, on_delete=models.CASCADE, related_name='comments'): Each comment is linked to a post.
🔹 is_approved = models.BooleanField(default=True): Used to filter out spam comments.

3️⃣ **Using Django ORM Queries in Views**
🟢 **Fetching All Published Posts**
📌 `Dynamically passes posts to home.html.`


🟠 **Fetching a Single Post (With Comments)**
📌 `F('views') + 1 ensures atomic database updates.`

🔵 **Fetching Most Commented Posts**
📌 `annotate(Count('comments')) adds a new field to count comments dynamically.`

🟣 **Fetching Posts with a Specific Tag**
📌 `Uses ManyToManyField reverse lookup via tag.posts.all().`

