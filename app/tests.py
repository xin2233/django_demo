from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from .models import User


class UserTestCase(TestCase):
    """
    def setUp(self)：用来初始化环境，包括创建初始数据，或做一些其他准备工作
    def test_xxx(self)：xxx可以是任何东西，以test_开头的方法，都会被django认为是需要测试的方法，跑测试时会被执行。
        注：每个需要被测试的方法都是相互独立的
    def tearDown(self)：跟setUp相对，用来清理测试环境和测试数据（在django中可以不关心这个）
    """
    def setUp(self):
        print('setUp')
        User.objects.create(
            name='stu1',
            sex=1,
            email='test1@qq.com',
            qq='333',
            phone='111',
        )

    # 测试数据创建以及sex字段的正确展示
    def test_create_and_sex_show(self):
        print('test_create_and_sex_show')
        User = User.objects.create(
            name='huyang',
            sex=1,
            email='test2@qq.com',
            profession='t1',
            qq='123',
            phone='test2123',
        )
        # django提供了get_xxx_display方法，可以替换sex_show
        self.assertEqual(User.sex_show, '男', '性别字段内容跟展示不一样')
        # self.assertEqual(User.get_sex_display, '男', '性别字段内容跟展示不一样')

    # 测试查询是否可用
    def test_filter(self):
        print('test_filter')
        User.objects.create(
            name='huyang',
            sex=1,
            email='testfilter@qq.com',
            profession='t2',
            qq='222',
            phone='22322',
        )
        name = 'stu1'
        Users = User.objects.filter(name=name)
        self.assertEqual(Users.count(), 1, '应该只存在一个名称为{}的记录'.format(name))

    # 测试首页的可用性
    def test_get_index(self):
        print('test_get_index')
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    # 测试post请求
    def test_post_User(self):
        print('test_post_User')
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='333@dd.com',
            profession='t2',
            qq='2323',
            phone='3222'
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        with open('temp.html', 'wb') as f:
            f.write(response.content)
        self.assertTrue(b'test_for_post' in response.content,
                        'response content must contain `test_for_post`')
