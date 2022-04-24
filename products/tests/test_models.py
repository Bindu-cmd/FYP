from calendar import c
from django.test import TestCase

from products.models import BookNow, Cart, Category, Order, Product

from django.contrib.auth.models import User


class TestProductModel(TestCase):

    def test_should_create_category(self):
        category_name="action"
        category=Category(category_name=category_name)
        category.save()
        self.assertEqual(category.category_name,category_name)

    def test_should_create_product(self):
        category_name="action"
        category=Category(category_name=category_name)
        category.save()

        product_name = ""
        product_price = 0.0
        stock = 0
        image = ""
        description=""
        created_at = ""
        authorname=""

        product=Product(
            product_name=product_name,
            product_price=product_price,
            stock=stock,
            image=image,
            category=category,
            description=description,
            authorname=authorname
        )
        product.save()
        self.assertEqual(product_name,product.product_name)
    
    def test_should_create_book(self):
        category_name="action"
        category=Category(category_name=category_name)
        category.save()
        bookname =""
        authorname=""
        publisher=""
        pages=1
        description=""
        publish_year=2200
        cover_image=""
        pdf_file=""

        book=BookNow(
            bookname =bookname,
            authorname=authorname,
            category=category,
            publisher=publisher,
            pages=pages,
            description=description,
            publish_year=publish_year,
            cover_image=cover_image,
            pdf_file=pdf_file
        )
        book.save()
        self.assertEqual(bookname,book.bookname)

    def test_should_create_order(self):
        category_name="action"
        category=Category(category_name=category_name)
        category.save()

        product_name = ""
        product_price = 0.0
        stock = 0
        image = ""
        description=""
        created_at = ""
        authorname=""

        product=Product(
            product_name=product_name,
            product_price=product_price,
            stock=stock,
            image=image,
            category=category,
            description=description,
            authorname=authorname
        )
        product.save()

        username = "bindu_asdf"
        email = "bindu@gmail.com"
        pass1 = "asdf123456fdsa"

        myuser = User.objects.create_user(username=username, email=email, password=pass1)


        quantity=1
        total_price=500
        payment_method='Esewa'
        contact_no="98438520713"
        address="Kathmandu"

        order = Order(
            product=product,
            user=myuser,
            quantity=quantity,
            total_price=total_price,
            payment_method=payment_method,
            contact_no=contact_no,
            address=address
        )
        self.assertEqual(order.user,myuser)
        self.assertEqual(order.product,product)


    def test_should_create_cart(self):
        category_name="action"
        category=Category(category_name=category_name)
        category.save()

        product_name = ""
        product_price = 0.0
        stock = 0
        image = ""
        description=""
        created_at = ""
        authorname=""

        product=Product(
            product_name=product_name,
            product_price=product_price,
            stock=stock,
            image=image,
            category=category,
            description=description,
            authorname=authorname
        )
        product.save()

        username = "bindu_asdf"
        email = "bindu@gmail.com"
        pass1 = "asdf123456fdsa"

        myuser = User.objects.create_user(username=username, email=email, password=pass1)

        cart = Cart(
            user=myuser,
            product=product
        )

        self.assertNotEqual(cart,None)
    