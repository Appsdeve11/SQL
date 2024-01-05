@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    tags = post.tags  # Retrieve tags 
    return render_template('post.html', post=post, tags=tags)