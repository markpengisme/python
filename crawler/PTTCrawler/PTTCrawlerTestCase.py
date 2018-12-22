from PTTCrawler import *
import unittest


class PTTCrawlerTestCase(unittest.TestCase):

	def test_get_web_page(self): 
		print("\ntest_get_web_page case start\n=======================")
		ptt = PTTCrawler("Gossiping")
		self.assertNotEqual(ptt.get_web_page(PTTCrawler.PTT_URL + '/bbs/Gossiping/index.html'),None)

	def test_get_articles(self):
		print("\ntest_get_articles case start\n=======================")
		ptt = PTTCrawler("joke")
		first_page = ptt.get_web_page(PTTCrawler.PTT_URL + '/bbs/NBA/index.html')
		ptt.get_articles(first_page)

	def test_start_crawl_today(self):
		print("\ntest_start_crawl_today case start\n=======================")
		ptt = PTTCrawler("Stock")
		date = ptt.today[5:].lstrip("0")
		ptt.start_crawl_today()
		for article in ptt.articles:
			self.assertEqual(article['date'],date)

	def test_start_crawl_all(self):
		print("\ntest_start_crawl_all case start\n=======================")
		ptt = PTTCrawler("NTUST_STUDY")
		ptt.start_crawl_all()
		self.assertNotEqual(len(ptt.articles),0)

	def test_get_the_point(self):
		print("\ntest_get_the_point case start\n=======================")
		ptt = PTTCrawler("Food")
		ptt.start_crawl_today()
		ptt.get_the_point(99)


	def test_dump_ptt(self):
		print("\ntest_dump_ptt case start\n=======================")
		ptt = PTTCrawler("C_CHAT")
		ptt.start_crawl_today()
		file_path = "C_CHAT.json"
		ptt.dump_ptt()
		self.assertTrue(os.path.isfile(file_path),True)
		os.remove(file_path)

	def test_empty_articles(self):
		print("\ntest_empty_articles case start\n=======================")
		ptt = PTTCrawler("NBA")
		self.assertEqual(ptt.articles,[])
		ptt.start_crawl_today()
		self.assertNotEqual(ptt.articles,[])
		ptt.empty_articles()
		self.assertEqual(ptt.articles,[])





if __name__ == '__main__':
	unittest.main()