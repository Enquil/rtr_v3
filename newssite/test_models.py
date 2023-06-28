from django.test import TestCase
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):

    def setUp(self):
        category_model = Category.objects.create(
            friendly_name='General',
        )
        category_model = Category.objects.create(
            friendly_name='Art and Entertainment',
        )

    def test_category_names(self):
        category_a = Category.objects.get(
            friendly_name='General'
        )
        category_b = Category.objects.get(
            friendly_name='Art and Entertainment'
        )
        self.assertEqual(category_a.name, 'general')
        self.assertEqual(category_b.name, 'art_entertainment')


class PostModelTest(TestCase):
    '''
    Test class for model: Post
    '''
    def setUp(self):

        category_model = Category.objects.create(
            friendly_name='General',
        )

        category_model = Category.objects.create(
            friendly_name='General',
        )

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

        user2 = User.objects.create(
            username='ada',
            is_superuser=False,
            password='difference'
        )

        post = Post.objects.create(
            title='how to crack codes',
            author=user,
            content="so easy",
            category=category_model,
        )

        post2 = Post.objects.create(
            title='Calculating machines',
            author=user2,
            content="sometimes, 1 is 0",
            category=category_model,
        )

    def test_post_user(self):
        '''
        Checks post.username matches the User model attached to the post
        @ setUp()
        '''
        test_post = Post.objects.get(id=1)
        test_post2 = Post.objects.get(id=2)
        self.assertEqual(test_post.author.username, 'alan')
        self.assertEqual(test_post.author.username, 'ada')

    def test_post_slug(self):
        '''
        Checks the slugify function on the post model
        which was not declared @ setUp()
        '''
        test_post = Post.objects.get(id=1)
        test_post2 = Post.objects.get(id=2)
        self.assertEqual(test_post.slug, 'how-to-crack-codes-alan1')
        self.assertEqual(test_post2.slug, 'calculating-machines-ada2')

    def test_published_by_default(self):
        '''
        Checks that default status on
        '''
        test_post = Post.objects.get(id=1)
        test_post2 = Post.objects.get(id=2)
        self.assertEqual(test_post.status, 1)
        self.assertEqual(test_post2.status, 1)


class CommentModelTest(Testcase):

    def setUp(self):

        category_model = Category.objects.create(
            friendly_name='General',
        )

        category_model2 = Category.objects.create(
            friendly_name='Art and Entertainment'
        )

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma',
            email='a.turing@realmail.com'
        )

        user2 = User.objects.create(
            username='ada',
            is_superuser=False,
            password='difference',
            email='a.lovelace@realmail.com'
        )

        post = Post.objects.create(
            title='how to crack codes',
            author=user,
            content="so easy",
            category=category_model,
        )

        post2 = Post.objects.create(
            title='Calculating machines',
            author=user2,
            content="Sometimes, 1 is 0",
            category=category_model2,
        )

        comment = Comment.objects.create(
            post=post,
            author=user2,
            body='Great job Alan!'
        )

        comment2 = Comment.objects.create(

        )
