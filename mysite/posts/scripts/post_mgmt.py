from posts.models import Post

def create_copies(copies: int, title='dummy', body='auto gen from script', published=False):
    print('attempting to create copies')
    for n in range(copies):
        t = title + "_" + str(n)


        print('Copy[{}];\t \
            title[{}];\n\t \
            body[{}];\n\t'.format(n, t, body))
        p = Post(title=t, body=body)
        p.save()

        if published:
            p.publish()