from django.test import TestCase
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):
    '''
    Test class for model: Category
    '''

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
        self.assertEqual(test_post2.author.username, 'ada')

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


class CommentModelTest(TestCase):

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
            post=post2,
            author=user,
            body='This looks amazing!'
        )

        comment3 = Comment.objects.create(
            post=post2,
            author=user2,
            parent=comment2,
            body='Thanks!'
        )

    def test_comment_email(self):
        '''
        Checks if comment.email returns correct value through save()
        (If email is set @ User)
        Only the comment posted by alan should contain one
        '''
        test_comment = Comment.objects.get(id=1)
        test_comment2 = Comment.objects.get(id=2)

        self.assertEqual(test_comment.email, '')
        self.assertEqual(test_comment2.email, 'a.turing@realmail.com')

    def test_is_top_level_comment(self):
        '''
        Checks the is_top_level property of Comment model
        test_comment3 should return False since it is child of test_comment2
        '''
        test_comment = Comment.objects.get(id=1)
        test_comment2 = Comment.objects.get(id=2)
        test_comment3 = Comment.objects.get(id=3)

        self.assertTrue(test_comment.is_top_level)
        self.assertTrue(test_comment2.is_top_level)
        self.assertFalse(test_comment3.is_top_level)

    def test_children(self):
        '''
        Checks if .children returns correctly by using
        .count() on the children <Queryset> for each comment
        - Only comment2 should have a child
        '''
        test_comment = Comment.objects.get(id=1)
        test_comment2 = Comment.objects.get(id=2)
        test_comment3 = Comment.objects.get(id=3)

        self.assertEqual(test_comment.children.count(), 0)
        self.assertEqual(test_comment2.children.count(), 1)
        self.assertEqual(test_comment3.children.count(), 0)
