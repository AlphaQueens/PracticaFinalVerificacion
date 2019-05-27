import unittest, mock, pytest
from views import delete_bad_chars, delete_stop_words, delete_numbers_from_string, clean_tweets, conection, remove_links

class old_tests(unittest.TestCase):

    def test_function_bad_chars(self):
        str="hola mi / nombre ** es pablo & * = ? ¿ garcia rubio )"
        assert(delete_bad_chars(str))=="hola mi   nombre    es pablo           garcia rubio  "

    def test_function_bad_chars_2(self):
        str="Esto???? es* una prueba/ para// hacer =··¿¿¿test"
        assert(delete_bad_chars(str))=="Esto     es  una prueba  para   hacer       test"

    def test_with_only_stop_words(self):
        str="que soy esto es una"
        assert(delete_stop_words(str))==''

    def test_links(self):
        str="https://t.co/InLYmEQr1d"
        assert(remove_links(str))==''


    def test_links_with_chars(self):
        str="https://t.co/InLYmEQr1d pablo alvaro"
        assert(remove_links(str))==' pablo alvaro'

    def test_stop_words(self):
        str="que soy esto es una verificacion y desarrollo"
        assert(delete_stop_words(str))=='verificacion desarrollo'

    def test_function_number(self):
        str="0 1 2 3 4 5 6 7 8 9 10 1234456789"
        assert(delete_numbers_from_string(str))=='           '

class Test(unittest.TestCase):
    @mock.patch('views.delete_bad_chars')
    def test_bad_chars(self,mock_delete_bad_chars):
        str1="Hola que haces? hola"
        mock_delete_bad_chars.return_value(str1)
        delete_bad_chars(str1)
        assert(delete_bad_chars(str1))=="Hola que haces  hola"

class Test2(unittest.TestCase):
    @mock.patch('views.clean_tweets')
    def test_empty_tweets(self,mock_clean_tweets):
        empty_tweet=" "
        mock_clean_tweets.return_value(empty_tweet)
        clean_tweets(empty_tweet)
        assert(clean_tweets(empty_tweet))==[]

class Test3(unittest.TestCase):
    @mock.patch('views.conection')
    def test_empty_tweets(self,mock_conection):
        value=True
        mock_conection.return_value(value)
        if conection():
            assert(conection())==True
        else:
            with pytest.raises(TypeError):
                conection()
