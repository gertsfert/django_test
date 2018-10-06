from posts.models import Post, Comment
from django.shortcuts import get_object_or_404

def create_posts(copies: int, title='dummy', body='auto gen from script', published=False):
    print('attempting to create posts')
    for n in range(copies):
        t = title + "_" + str(n)


        print('Copy[{}];\t \
            title[{}];\n\t \
            body[{}];\n\t'.format(n, t, body))
        p = Post(title=t, body=body)
        p.save()

        if published:
            p.publish()

def create_comments(
    copies: int, 
    post_id: int, 
    author_id:int=1, 
    body='auto gen from script', 
    approved=False):

    print('attempting to create comments')

    for n in range(copies):
        print('Copy[{}];\t \
            post_id[{}];\n\t \
            author_id[{}];\n\t \
            approved[{}];'.format(n, post_id, author_id, approved))

        p = get_object_or_404(Post, id=post_id)
        c = Comment(post=p, author=author_id, body=body)

        if approved:
            c.approve()