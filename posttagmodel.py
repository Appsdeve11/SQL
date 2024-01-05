class PostTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))

    def __init__(self, post_id, tag_id):
        self.post_id = post_id
        self.tag_id = tag_id

# Create database tables
db.create_all()