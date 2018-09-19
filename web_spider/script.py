import sys
import time


# (category, sub, url)
metadata = [
	("Business & Finance", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_0?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284819011&bbn=13727922011&ie=UTF8&qid=1537298359&rnid=13727922011"), 
	("Communications", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_1?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284865011&bbn=13727922011&ie=UTF8&qid=1537300190&rnid=13727922011"),
	("Connected Car", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_2?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284820011&bbn=13727922011&ie=UTF8&qid=1537298477&rnid=13727922011"),
	("Education & Reference", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_3?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284821011&bbn=13727922011&ie=UTF8&qid=1537298514&rnid=13727922011"),
	("Food & Drink", "Restaurant Booking, Info & Reviews", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajel1_ct_x_ct00_w?_encoding=UTF8&node=14284825011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=12GRDRDX8E9FYQKQSFPA&pf_rd_r=12GRDRDX8E9FYQKQSFPA&pf_rd_t=101&pf_rd_p=95dffcc4-0382-5f4f-95d3-13d042be29b8&pf_rd_p=95dffcc4-0382-5f4f-95d3-13d042be29b8&pf_rd_i=14284822011"),
	("Food & Drink", "Cooking & Recipes", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajel1_ct_x_ct01_w?_encoding=UTF8&node=14284823011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=12GRDRDX8E9FYQKQSFPA&pf_rd_r=12GRDRDX8E9FYQKQSFPA&pf_rd_t=101&pf_rd_p=95dffcc4-0382-5f4f-95d3-13d042be29b8&pf_rd_p=95dffcc4-0382-5f4f-95d3-13d042be29b8&pf_rd_i=14284822011"),
	("Food & Drink", "Delivery & Takeout", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajel1_ct_x_ct02_w?_encoding=UTF8&node=14284824011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=12GRDRDX8E9FYQKQSFPA&pf_rd_r=12GRDRDX8E9FYQKQSFPA&pf_rd_t=101&pf_rd_p=95dffcc4-0382-5f4f-95d3-13d042be29b8&pf_rd_p=95dffcc4-0382-5f4f-95d3-13d042be29b8&pf_rd_i=14284822011"),
	("Food & Drink", "Wine & Beverages", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajel1_ct_x_ct03_w?_encoding=UTF8&node=14284826011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=12GRDRDX8E9FYQKQSFPA&pf_rd_r=12GRDRDX8E9FYQKQSFPA&pf_rd_t=101&pf_rd_p=95dffcc4-0382-5f4f-95d3-13d042be29b8&pf_rd_p=95dffcc4-0382-5f4f-95d3-13d042be29b8&pf_rd_i=14284822011"),
	("Games, Trivia & Accessories", "Games", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajg3f_ct_x_ct00_w?_encoding=UTF8&node=14284829011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=TJ5ES8KT82WARYBDH56H&pf_rd_r=TJ5ES8KT82WARYBDH56H&pf_rd_t=101&pf_rd_p=abb81530-a51b-5089-b292-0f596383e5d2&pf_rd_p=abb81530-a51b-5089-b292-0f596383e5d2&pf_rd_i=14284827011"),
	("Games, Trivia & Accessories", "Knowledge & Trivia", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajg3f_ct_x_ct01_w?_encoding=UTF8&node=14284830011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=TJ5ES8KT82WARYBDH56H&pf_rd_r=TJ5ES8KT82WARYBDH56H&pf_rd_t=101&pf_rd_p=abb81530-a51b-5089-b292-0f596383e5d2&pf_rd_p=abb81530-a51b-5089-b292-0f596383e5d2&pf_rd_i=14284827011"),
	("Games, Trivia & Accessories", "Game Info & Accessories", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajg3f_ct_x_ct02_w?_encoding=UTF8&node=14284828011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=TJ5ES8KT82WARYBDH56H&pf_rd_r=TJ5ES8KT82WARYBDH56H&pf_rd_t=101&pf_rd_p=abb81530-a51b-5089-b292-0f596383e5d2&pf_rd_p=abb81530-a51b-5089-b292-0f596383e5d2&pf_rd_i=14284827011"),
	("Health & Fitness", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_6?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284831011&bbn=13727922011&ie=UTF8&qid=1537298764&rnid=13727922011"),
	("Home Services", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_7?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A17388364011&bbn=13727922011&ie=UTF8&qid=1537298764&rnid=13727922011"),
	("Kids", "Education & Reference", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajhMJ_ct_x_ct00_w?_encoding=UTF8&node=14284833011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=869JYY3N0Q0V0YE2FZ5J&pf_rd_r=869JYY3N0Q0V0YE2FZ5J&pf_rd_t=101&pf_rd_p=892e880c-b60c-51e5-b730-d70b76c3324d&pf_rd_p=892e880c-b60c-51e5-b730-d70b76c3324d&pf_rd_i=14284832011"),
	("Kids", "Games", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajhMJ_ct_x_ct01_w?_encoding=UTF8&node=14284834011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=869JYY3N0Q0V0YE2FZ5J&pf_rd_r=869JYY3N0Q0V0YE2FZ5J&pf_rd_t=101&pf_rd_p=892e880c-b60c-51e5-b730-d70b76c3324d&pf_rd_p=892e880c-b60c-51e5-b730-d70b76c3324d&pf_rd_i=14284832011"),
	("Kids", "Music & Audio", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajhMJ_ct_x_ct02_w?_encoding=UTF8&node=14284835011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=869JYY3N0Q0V0YE2FZ5J&pf_rd_r=869JYY3N0Q0V0YE2FZ5J&pf_rd_t=101&pf_rd_p=892e880c-b60c-51e5-b730-d70b76c3324d&pf_rd_p=892e880c-b60c-51e5-b730-d70b76c3324d&pf_rd_i=14284832011"),
	("Kids", "Novelty & Humor", "https://www.amazon.com/b/ref=s9_acsd_hfnv_hd_bw_bFajhMJ_ct_x_ct03_w?_encoding=UTF8&node=14284836011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=869JYY3N0Q0V0YE2FZ5J&pf_rd_r=869JYY3N0Q0V0YE2FZ5J&pf_rd_t=101&pf_rd_p=892e880c-b60c-51e5-b730-d70b76c3324d&pf_rd_p=892e880c-b60c-51e5-b730-d70b76c3324d&pf_rd_i=14284832011"),
	("Lifestyle", "Astrology", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_0?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284838011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "Cooking & Recipes", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_1?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284823011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "Event Finders", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_2?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284839011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "Fashion & Style", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_3?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284840011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "Friends & Family", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_4?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284867011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "Health & Fitness", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_5?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284831011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "Home Services", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_6?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A17388364011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "Pets & Animals", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_7?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284841011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "Religion & Spirituality", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_8?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284842011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "Self Improvement", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_9?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284843011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "To-Do Lists & Notes", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_10?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284861011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Lifestyle", "Wine & Beverages", "https://www.amazon.com/s/ref=lp_14284837011_nr_n_11?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284837011%2Cn%3A14284826011&bbn=14284837011&ie=UTF8&qid=1537298968&rnid=14284837011"),
	("Local", "Event Finders", "https://www.amazon.com/s/ref=lp_14284844011_nr_n_0?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284844011%2Cn%3A14284839011&bbn=14284844011&ie=UTF8&qid=1537299187&rnid=14284844011"),
	("Local", "Food Delivery & Takeout", "https://www.amazon.com/s/ref=lp_14284844011_nr_n_1?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284844011%2Cn%3A14284824011&bbn=14284844011&ie=UTF8&qid=1537299187&rnid=14284844011"),
	("Local", "Movie Showtimes", "https://www.amazon.com/s/ref=lp_14284844011_nr_n_2?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284844011%2Cn%3A14284849011&bbn=14284844011&ie=UTF8&qid=1537299187&rnid=14284844011"),
	("Local", "Public Transportation", "https://www.amazon.com/s/ref=lp_14284844011_nr_n_3?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284844011%2Cn%3A14284879011&bbn=14284844011&ie=UTF8&qid=1537299187&rnid=14284844011"),
	("Local", "Restaurant Booking, Info & Reviews", "https://www.amazon.com/s/ref=lp_14284844011_nr_n_4?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284844011%2Cn%3A14284825011&bbn=14284844011&ie=UTF8&qid=1537299187&rnid=14284844011"),
	("Local", "Schools", "https://www.amazon.com/s/ref=lp_14284844011_nr_n_5?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284844011%2Cn%3A14284845011&bbn=14284844011&ie=UTF8&qid=1537299187&rnid=14284844011"),
	("Local", "Taxi & Ridesharing", "https://www.amazon.com/s/ref=lp_14284844011_nr_n_6?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284844011%2Cn%3A14284880011&bbn=14284844011&ie=UTF8&qid=1537299187&rnid=14284844011"),
	("Movies & TV", "Knowledge & Trivia", "https://www.amazon.com/s/ref=lp_14284846011_nr_n_0?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284846011%2Cn%3A14284847011&bbn=14284846011&ie=UTF8&qid=1537299339&rnid=14284846011"),
	("Movies & TV", "Movie Info & Reviews", "https://www.amazon.com/s/ref=lp_14284846011_nr_n_1?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284846011%2Cn%3A14284848011&bbn=14284846011&ie=UTF8&qid=1537299339&rnid=14284846011"),
	("Movies & TV", "Movie Showtimes", "https://www.amazon.com/s/ref=lp_14284846011_nr_n_2?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284846011%2Cn%3A14284849011&bbn=14284846011&ie=UTF8&qid=1537299339&rnid=14284846011"),
	("Movies & TV", "TV Guides", "https://www.amazon.com/s/ref=lp_14284846011_nr_n_3?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284846011%2Cn%3A14284850011&bbn=14284846011&ie=UTF8&qid=1537299339&rnid=14284846011"),
	("Music & Audio", "Accessories", "https://www.amazon.com/s/ref=lp_14284851011_nr_n_0?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284851011%2Cn%3A14284852011&bbn=14284851011&ie=UTF8&qid=1537299439&rnid=14284851011"),
	("Music & Audio", "Knowledge & Trivia", "https://www.amazon.com/s/ref=lp_14284851011_nr_n_1?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284851011%2Cn%3A14284853011&bbn=14284851011&ie=UTF8&qid=1537299439&rnid=14284851011"),
	("Music & Audio", "Music Info, Reviews & Recognition Services", "https://www.amazon.com/s/ref=lp_14284851011_nr_n_2?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284851011%2Cn%3A14284854011&bbn=14284851011&ie=UTF8&qid=1537299439&rnid=14284851011"),
	("Music & Audio", "Podcasts", "https://www.amazon.com/s/ref=lp_14284851011_nr_n_3?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284851011%2Cn%3A14284855011&bbn=14284851011&ie=UTF8&qid=1537299439&rnid=14284851011"),
	("Music & Audio", "Streaming Services", "https://www.amazon.com/s/ref=lp_14284851011_nr_n_4?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284851011%2Cn%3A14284856011&bbn=14284851011&ie=UTF8&qid=1537299439&rnid=14284851011"),
	("News", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_13?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284857011&bbn=13727922011&ie=UTF8&qid=1537299559&rnid=13727922011"),
	("Novelty & Humor", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_14?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284858011&bbn=13727922011&ie=UTF8&qid=1537299574&rnid=13727922011"),
	("Productivity", "Alarms & Clocks", "https://www.amazon.com/s/ref=lp_14284859011_nr_n_0?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284859011%2Cn%3A14284883011&bbn=14284859011&ie=UTF8&qid=1537299598&rnid=14284859011"),
	("Productivity", "Calculators", "https://www.amazon.com/s/ref=lp_14284859011_nr_n_1?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284859011%2Cn%3A14284884011&bbn=14284859011&ie=UTF8&qid=1537299598&rnid=14284859011"),
	("Productivity", "Calendars & Reminders", "https://www.amazon.com/s/ref=lp_14284859011_nr_n_2?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284859011%2Cn%3A14284885011&bbn=14284859011&ie=UTF8&qid=1537299598&rnid=14284859011"),
	("Productivity", "Communications", "https://www.amazon.com/s/ref=lp_14284859011_nr_n_3?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284859011%2Cn%3A14284865011&bbn=14284859011&ie=UTF8&qid=1537299598&rnid=14284859011"),
	("Productivity", "Organizers & Assistants", "https://www.amazon.com/s/ref=lp_14284859011_nr_n_4?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284859011%2Cn%3A14284860011&bbn=14284859011&ie=UTF8&qid=1537299598&rnid=14284859011"),
	("Productivity", "Self Improvement", "https://www.amazon.com/s/ref=lp_14284859011_nr_n_5?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284859011%2Cn%3A14284843011&bbn=14284859011&ie=UTF8&qid=1537299598&rnid=14284859011"),
	("Productivity", "To-Do Lists & Notes", "https://www.amazon.com/s/ref=lp_14284859011_nr_n_6?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284859011%2Cn%3A14284861011&bbn=14284859011&ie=UTF8&qid=1537299598&rnid=14284859011"),
	("Productivity", "Translators", "https://www.amazon.com/s/ref=lp_14284859011_nr_n_7?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284859011%2Cn%3A14284881011&bbn=14284859011&ie=UTF8&qid=1537299598&rnid=14284859011"),
	("Shopping", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_16?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284862011&bbn=13727922011&ie=UTF8&qid=1537299725&rnid=13727922011"),
	("Smart Home", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_17?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284863011&bbn=13727922011&ie=UTF8&qid=1537299742&rnid=13727922011"),
	("Social", "Communications", "https://www.amazon.com/s/ref=lp_14284864011_nr_n_0?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284864011%2Cn%3A14284865011&bbn=14284864011&ie=UTF8&qid=1537299764&rnid=14284864011"),
	("Social", "Dating", "https://www.amazon.com/s/ref=lp_14284864011_nr_n_1?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284864011%2Cn%3A14284866011&bbn=14284864011&ie=UTF8&qid=1537299764&rnid=14284864011"),
	("Social", "Friends & Family", "https://www.amazon.com/s/ref=lp_14284864011_nr_n_2?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284864011%2Cn%3A14284867011&bbn=14284864011&ie=UTF8&qid=1537299764&rnid=14284864011"),
	("Social", "Social Networking", "https://www.amazon.com/s/ref=lp_14284864011_nr_n_3?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284864011%2Cn%3A14284868011&bbn=14284864011&ie=UTF8&qid=1537299764&rnid=14284864011"),
	("Sports", "Exercise & Workout", "https://www.amazon.com/s/ref=lp_14284869011_nr_n_0?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284869011%2Cn%3A14284870011&bbn=14284869011&ie=UTF8&qid=1537299838&rnid=14284869011"),
	("Sports", "Games", "https://www.amazon.com/s/ref=lp_14284869011_nr_n_1?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284869011%2Cn%3A14284871011&bbn=14284869011&ie=UTF8&qid=1537299838&rnid=14284869011"),
	("Sports", "News", "https://www.amazon.com/s/ref=lp_14284869011_nr_n_2?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284869011%2Cn%3A14284872011&bbn=14284869011&ie=UTF8&qid=1537299838&rnid=14284869011"),
	("Sports", "Score Keeping", "https://www.amazon.com/s/ref=lp_14284869011_nr_n_3?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284869011%2Cn%3A14284873011&bbn=14284869011&ie=UTF8&qid=1537299838&rnid=14284869011"),
	("Travel & Transportation", "Currency Guides & Converters", "https://www.amazon.com/s/ref=lp_14284874011_nr_n_0?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284874011%2Cn%3A14284875011&bbn=14284874011&ie=UTF8&qid=1537299904&rnid=14284874011"),
	("Travel & Transportation", "Flight Finders", "https://www.amazon.com/s/ref=lp_14284874011_nr_n_1?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284874011%2Cn%3A14284876011&bbn=14284874011&ie=UTF8&qid=1537299904&rnid=14284874011"),
	("Travel & Transportation", "Hotel Finders", "https://www.amazon.com/s/ref=lp_14284874011_nr_n_2?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284874011%2Cn%3A14284877011&bbn=14284874011&ie=UTF8&qid=1537299904&rnid=14284874011"),
	("Travel & Transportation", "Navigation & Trip Planners", "https://www.amazon.com/s/ref=lp_14284874011_nr_n_3?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284874011%2Cn%3A14284878011&bbn=14284874011&ie=UTF8&qid=1537299904&rnid=14284874011"),
	("Travel & Transportation", "Public Transportation", "https://www.amazon.com/s/ref=lp_14284874011_nr_n_4?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284874011%2Cn%3A14284879011&bbn=14284874011&ie=UTF8&qid=1537299904&rnid=14284874011"),
	("Travel & Transportation", "Taxi & Ridesharing", "https://www.amazon.com/s/ref=lp_14284874011_nr_n_5?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284874011%2Cn%3A14284880011&bbn=14284874011&ie=UTF8&qid=1537299904&rnid=14284874011"),
	("Travel & Transportation", "Translators", "https://www.amazon.com/s/ref=lp_14284874011_nr_n_6?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284874011%2Cn%3A14284881011&bbn=14284874011&ie=UTF8&qid=1537299904&rnid=14284874011"),
	("Utilities", "Alarms & Clocks", "https://www.amazon.com/s/ref=lp_14284882011_nr_n_0?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284882011%2Cn%3A14284883011&bbn=14284882011&ie=UTF8&qid=1537300043&rnid=14284882011"),
	("Utilities", "Calculators", "https://www.amazon.com/s/ref=lp_14284882011_nr_n_1?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284882011%2Cn%3A14284884011&bbn=14284882011&ie=UTF8&qid=1537300084&rnid=14284882011"),
	("Utilities", "Calendars & Reminders", "https://www.amazon.com/s/ref=lp_14284882011_nr_n_2?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284882011%2Cn%3A14284885011&bbn=14284882011&ie=UTF8&qid=1537300084&rnid=14284882011"),
	("Utilities", "Device Tracking", "https://www.amazon.com/s/ref=lp_14284882011_nr_n_3?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284882011%2Cn%3A14284886011&bbn=14284882011&ie=UTF8&qid=1537300084&rnid=14284882011"),
	("Utilities", "Translators", "https://www.amazon.com/s/ref=lp_14284882011_nr_n_4?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284882011%2Cn%3A14284881011&bbn=14284882011&ie=UTF8&qid=1537300084&rnid=14284882011"),
	("Utilities", "Unit Converters", "https://www.amazon.com/s/ref=lp_14284882011_nr_n_5?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284882011%2Cn%3A14284887011&bbn=14284882011&ie=UTF8&qid=1537300084&rnid=14284882011"),
	("Utilities", "Zip Code Lookup", "https://www.amazon.com/s/ref=lp_14284882011_nr_n_6?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284882011%2Cn%3A14284888011&bbn=14284882011&ie=UTF8&qid=1537300084&rnid=14284882011"),
	("Weather", "", "https://www.amazon.com/s/ref=lp_13727921011_nr_n_22?fst=as%3Aoff&rh=n%3A13727921011%2Cn%3A%2113727922011%2Cn%3A14284889011&bbn=13727922011&ie=UTF8&qid=1537300160&rnid=13727922011"),
]

i = sys.argv[1]

page = metadata[int(i)]
print(page[2])

"""
	command = "/bin/bash ./dumb.sh " + url
	os.system(command)
	time.sleep(2)"""














