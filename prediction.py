# -*- coding: utf-8 -*-
from sklearn import linear_model
import numpy as np
import pickle
import gzip
import csv

right1 = "Dear Conservative,This week, the GOP did the unthinkable: they caved and allowed Loretta Lynch to become the next attorney general.We have covered how lynch is rabidly anti-gun and supports Obama’s executive action on amnesty, but little has been discussed in the media about how pro-abortion this woman is.In 2006, Loretta Lynch signed an amicus brief sent to the Supreme Court arguing that the Federal partial-birth abortion ban was unconstitutional because the term 'living fetus' was 'hopelessly vague.' It doesn’t get more disgusting than this…Thanks to the spineless GOP, this woman is the chief law enforcement agent in the country. Some in the left have even moved beyond partial-birth abortions and begun advocating what they call after-birth abortion. No, this is not a joke. There are liberals who are advocating aborting children after they’ve already been born! Congress has completely buckled on protecting the rights of the unborn. Demand that they pass the Pain Capable Unborn Child Protection Act of 2015 and outlaw abortion after 20 weeks! At 20 weeks, unborn children feel pain. If surgeons need to operate on a child in utero, the child is given fetal anesthesia to alleviate the pain. Some doctors have witnessed in utero pain reactions as early as 18-weeks into a pregnancy. The fact of the matter is that doctors are ethically required to administer anesthesia to reduce the child’s pain and suffering. So how can it possibly be legal to kill a 20-week old baby? There is an abortion procedure known as dismemberment. It is exactly what it sounds like. As late as the second trimester, doctors kill the baby by literally dismembering it. I believe life begins at conception and it is horrifying to think that a child could undergo such a gruesome procedure and feel all of the accompanying pain. That is what the Pain Capable Unborn Child Protection Act of 2015 (HR 36) attempts to stop. When the unborn child reaches 20-weeks and is able to feel and register pain signals, he or she cannot be aborted. Period. Heck, we have laws against cruel and unusual punishment for criminals. There is a whole industry designed to implementing the death penalty with minimal pain. Yet while we spend millions and millions of dollars to painlessly kill murderers, nothing is being done to protect the unborn. Congress had a chance to pass this law earlier in the year, and they got cold feet. They left hundreds of thousands of March for Life demonstrators out in the cold. When the Supreme Court released its decision in Roe v Wade, it stated that it was unconscionable to abort a baby who had reached the developmental point of viability. The court defined viability as the moment a fetus could potentially survive outside of the womb, even with the help of medical aids. The Court left it up to Congress to delineate this point in gestation and the science supports outlawing abortion after 20-weeks. In 2011, a child was born in Europe at 21 weeks and survived, proving that the point of viability is much earlier than the Supreme Court believed in 1973. Another child was born at 21 weeks, 5 days gestation in 2006. Today, she is in Second Grade. Pro-abortion advocates believe that they have the right to abortion on-demand at any point in pregnancy. The reality is that numerous court cases support the right of states and the Federal government to outlaw abortions after the point of viability. When this bill was brought before Congress in January, the GOP spit in our faces and chickened out. We cannot allow that to happen again! Pressure is rising for Congress to pass this common-sense law. It is up to you to raise your voice and protect the rights of the unborn! Tell Congress that if the unborn can feel pain, they CANNOT be aborted! Sincerely, Joe Otto"
right2 = "The country is closely divided over abortion and fetal tissue research, yet tends to view Planned Parenthood favorably. The latest Fox News poll asks about these issues, as well as the secretly-shot videos that show Planned Parenthood employees talking about dollar amounts associated with fetal tissue and organs from abortions. Nearly half of voters have seen or heard about the videos (49 percent).  More self-identified pro-life voters (54 percent) report having seen the videos than pro-choice voters (46 percent). Among those familiar with the videos, 49 percent describe them as disturbing and would prefer to stop the use of fetal tissue from abortions in medical research.  Forty-three percent agree the videos are disturbing, but say the research should continue.Additional undercover videos were released since the poll was conducted.CLICK HERE TO READ THE POLL RESULTSThe numbers are about the same when all voters are asked generally about using organs and tissue from aborted human fetuses for medical research on deadly diseases:  48 percent approve vs. 47 percent disapprove.Majorities of Democrats (64 percent) and independents (56 percent) approve of fetal tissue research in general, while more than two-thirds of Republicans disapprove (69 percent).By a 52-42 percent margin, voters think Planned Parenthood should receive federal funding.   Groups most likely to support government funding include Democrats (79 percent), liberals (79 percent), blacks (79 percent), pro-choice voters (74 percent), young voters (64 percent), urbanites (61 percent) and women (55 percent).Those most likely to oppose federal funding include Republicans (72 percent), white evangelical Christians (69 percent), those in the Tea Party movement (69 percent), pro-life voters (64 percent), conservatives (61 percent) and regular church-goers (53 percent).In addition, more voters than not view Planned Parenthood positively: 50 percent have a favorable opinion, while 38 percent view it unfavorably.  Six percent say they have never heard of Planned Parenthood.Women (54 percent) are more likely than men (46 percent) and blacks (66 percent) are more likely than whites (46 percent) to have a positive view. There’s also a big difference among age groups, as 61 percent of voters under age 30 have a favorable opinion of Planned Parenthood compared to just 44 percent of those ages 55 and over.Democrats (74 percent) are more than three times as likely as Republicans (22 percent) to feel positively toward Planned Parenthood.  For independents, 52 percent have a favorable opinion.Meanwhile, 47 percent of voters consider themselves pro-choice, while 46 percent are pro-life.  Earlier this year more voters identified as pro-choice by a five-point margin (49 vs. 44 percent in April 2015).  Opinion has been narrowly divided on the abortion issue for years and which view is on top shifts back and forth. The Fox News poll is based on landline and cell phone interviews with 1,008 randomly chosen registered voters nationwide and was conducted under the joint direction of Anderson Robbins Research (D) and Shaw & Company Research (R) from August 11-13, 2015. The poll has a margin of sampling error of plus or minus three percentage points for all registered voters."
right3 = "The battle among Capitol Hill Republicans to replace House Speaker John Boehner will likely unfold like the one that led to Boehner's resignation: GOP leadership vs. the party's most conservative caucus.Before we rush headlong into leadership elections, we need to take time to reflect on what has happened and have a serious discussion about … what we expect of our leaders, and how we plan to accomplish our goals, Illinois Rep. Peter Roskam said Saturday in a letter to fellow GOP House members. Members of Boehner's leadership team already appear to be positioning themselves for the job of running the Republican-controlled chamber. Among them is second-in-command House Majority Leader Kevin McCarthy.The California Republican has made no official statement, but sources tell Fox News that he is seeking the position. And Boehner said in his resignation announcement Friday that McCarthy would be an excellent speaker."
left1 = "During his historic speech at a joint meeting of Congress on Thursday, Pope Francis hit upon a variety of issues that have defined the Catholic church: protecting the environment, helping the poor, addressing the plight of immigrants, abolishing the death penalty and taking a stand against the proliferation of the weapons trade, to name a few.Yet, while the pope had strong words on many of these causes, he glossed over two other topics that American bishops have strongly lobbied against in recent years: abortion and same-sex marriage. In fact, he did not even mention them by name.In his wide-ranging 3,404-word address praising the democratic mission of Congress and the spirit of the American people -- touching upon Martin Luther King Jr., Abraham Lincoln, Dorothy Day and Thomas Merton -- the pope called for action to protect refugees, eliminate capital punishment and stop war, yet used a mere 21 words to allude to abortion and only 54 to touch vaguely upon the fact that same-sex marriage is now legal across the United States.On abortion, the pope’s comments were tucked into a larger discussion on the the Golden Rule, which reminds us of our responsibility to protect and defend human life at every stage of its development. But he did not say the word abortion.On marriage, the pope had a few more words. I cannot hide my concern for the family, which is threatened, perhaps as never before, from within and without. Fundamental relationships are being called into question, as is the very basis of marriage and the family. I can only reiterate the importance and, above all, the richness and the beauty of family life.Yet, Francis, who was notably the first pope to use the word gay -- as he did during his famed Who I am to judge? interview -- and who has been praised and criticized by LGBT activists for his words on the spirituality of gay people, did not explicitly mention same-sex marriage.U.S. Catholic bishops, by comparison, have lobbied intensely in recent years against abortion, contraception and same-sex marriage, encouraging homilies and teach-ins on the issues on the parish level and hosting extensive policy pages about those topics on the U.S. Conference of Catholic Bishops website. Bishops have also lobbied against the death penalty, which the pope mentioned in his speech, and on behalf of immigrants and the poor.By no means does Francis support abortion or gay marriage -- but his decision to largely skip over the topics during his speech to Congress is notable, and likely won’t gain him fans among conservative Catholics, who have already criticized the pope for his off-the-cuff remarks on social issues and for his views on climate change.Yesterday, Pope Francis said that promoting life and family were the major reason he came to America this week. Yet, disappointingly, the pope did not mention abortion by name in his address to Congress, said John-Henry Westen, the editor-in-chief of LifeSiteNews, a conservative Catholic website.Francis has already indicated that his focus as pope is not on sexuality or culture war-related issues. In a landmark interview just six months after he became pope in 2013, he said the church was obsessed with abortion, contraception and gay marriage.It is not necessary to talk about these issues all the time. The dogmatic and moral teachings of the church are not all equivalent. The church’s pastoral ministry cannot be obsessed with the transmission of a disjointed multitude of doctrines to be imposed insistently, he said in the interview with Rev. Antonio Spadaro, who edits La Civiltà Cattolica, an Italian Jesuit publication.We have to find a new balance, the pope said at the time. Otherwise, even the moral edifice of the church is likely to fall like a house of cards, losing the freshness and fragrance of the Gospel."
left2 = "Pope Francis: Priests Can Forgive Abortion If Women Are 'Contrite'. Pope Francis will allow Roman Catholic priests to absolve women who have had abortions if they seek forgiveness during the upcoming Holy Year of Mercy, the Vatican announced Tuesday.  The pontiff said he will allow priests discretion to absolve of the sin of abortion those who have procured it and who, with contrite heart, seek forgiveness for it during the special year, beginning December 8.  I am well aware of the pressure that has led [women] to this decision, he wrote in the announcement. I know that it is an existential and moral ordeal. Pope Francis Riccardo De Luca / AP Abortion is considered a grave sin by the Catholic church, and those who seek it are usually excommunicated. In normal circumstances, forgiveness can only be granted by senior church figures.  Deputy Vatican spokesman Father Ciro Benedettini told Reuters that for now the change would apply only during the Holy Year. The pope's letter did not mention people who perform abortions.  Pope Francis announced in March that the Holy Year, which runs until Nov. 20, 2016, was a way to promote inclusiveness, saying the church could make more evident its mission to be a witness of mercy. Abortion has been front and center for many American bishops In a letter published online on Tuesday, he said: The experience of mercy, indeed, becomes visible in the witness of concrete signs as Jesus himself taught us.  He also offered an olive branch to Catholics who worship with a breakaway group called the Fraternity of St Pius X. I trust that in the near future solutions may be found to recover full communion with the priests and superiors of the fraternity, he wrote.  John L. Allen Jr., a Catholic commentator and associate editor of the Crux website, said the pope's announcement should not be seen as a change to official teaching.   Both abortion and defiance of papal authority are still considered grave sins resulting in excommunication, he wrote. In effect, what Francis has done instead of changing doctrine is to extend the range of mercy to anyone who seeks forgiveness with what he describes as a 'contrite heart.'  Allen said the temporary concession on abortion likely will be welcomed by many Catholic liberals, but added that there could be blowback from conservatives.  Andrew Chesnut, professor of religion at Virginia Commonwealth University, said the Francis' announcement consolidates his reputation as the pope of mercy and as a master strategist in the effort to bring back lapsed Catholics into the fold.  Ironically, his native Latin America, home to 40 percent of the world's Catholics, has the highest abortion rate of any region on earth, Chestnut said. Scores of women there and around the world have been compelled to leave the Church for committing what's considered a grave sin. His one-year jubilee also comes on the eve of his visit to the U.S., where abortion has been front and center for many American bishops.   Father Thomas J. Reese, author of Inside the Vatican: The Politics and Organization of the Catholic Church, said the pope's message was consistent with his desire to stress on the compassion and mercy of God.  Reese added: He has compared the Church to a field hospital, which cares for the wounded rather than berating them.  The Holy Year is one of the 1.2 billion-member church's most important events, and sees faithful make pilgrimages to Rome and other religious sites around the world."
left3 = "The conclusion of a sweeping new nationwide study released today that included interviews with every known abortion provider in the country is unambiguous. Abortions are decreasing.The study, conducted by the Guttmacher Institute, which researches issues related to reproductive health and sexuality, found that in 2005, the U.S. abortion rate fell to 19.4 abortions per 1,000 women between the ages of 15 to 44, the lowest level since 1974. The total number of abortions also declined, to a total of 1.2 million in 2005, well below the all-time high of 1.6 million abortions in 1990.But the study raises a fascinating and tricky question: Why?The researchers who conducted the study said they simply don't know, but they do have two theories.One reason could be that since people now have easier access to contraception -- including emergency contraception like Plan B -- there are fewer unwanted pregnancies.Another reason could be that there are also fewer abortion clinics.Eighty-seven percent of counties in the United States don't have an abortion provider, Rachel Jones of the Guttmacher Institute said. Thirty-five percent of women live in those counties.Activists on both sides of this debate have their own theories, and everyone's claiming victory.Supporters of abortion rights say the decline is the result of the sex education and family planning they provide.Opponents say more women are coming to grips with the horror of abortion, in part because of the increasing numbers of so-called crisis pregnancy centers, which set up near abortion clinics and offer services like ultrasounds to convince women to keep their babies.This is a very powerful tool, anti-abortion activist Chris Slattery said of ultrasounds. Now it's much harder for them to actually think of destroying a child.Pomona College political science professor John Seery, who studies the politics of abortion, has his own theory, which he calls the Juno effect after the current movie in which a young woman decides to keep her baby for personal not political reasons. He said the movie reflects a cultural shift in the country.I think the filmmakers were onto something. Seery said.The political and policy debate over abortion is as divisive and deadlocked as ever, even 35 years after the Roe v. Wade Supreme Court decision. But the study released today indicates that on a personal level, women are choosing to have fewer abortions."


right = ['I am pro-life.', 'Everyone has the right to life.']
left = ['I am pro-choice.', 'Everyone has the right to an abortion']
new = ['Everyone has an abortion.', 'Everyone needs to make their own choice.', 'x', 'right']

def convert_file_to_string(filename):
	string = ''
	with open(filename) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			for sentence in row:
				string += sentence
	return string


def string_to_word_list(string):
	"""
	Converts a string (title or article) into a list of string_to_word_list.
	Data processing helper function.
	"""
	word_list = []
	word = ''
	for char in string:
		if char.isalnum():
			word += char
		else:
			if word != '':
				# If the word only contains letters
				if word.isalpha():
					word_list.append(word.lower())
				# If the word contains at least 1 number
				else:
					word_list.append('xxnumberxx')
				word = ''
	if word != '':
		word_list.append(word)
	return word_list


def get_all_words(articles):
	"""
	Returns a sorted list of all words from all articles inputted
	"""
	word_list = []
	for article in articles:
		word_list += string_to_word_list(article)
	word_list = list(set(word_list))
	return sorted(word_list, key=str)


def get_freq_map(string):
	"""
	Given a string of words, calculates the frequency (as a decimal)
	of occurrences of each word in the sentence
	"""
	freq_dict = {}
	word_list = string_to_word_list(string)
	for word in word_list:
		if word in freq_dict.keys():
			freq_dict[word] += 1.0 / len(word_list)
		else:
			freq_dict[word] = 1.0 / len(word_list)
	return freq_dict


def create_article_vector(all_words, freq_map):
	"""
	Creates a vector out of an article's freq map to prepare data for training
	"""
	features = []
	for word in all_words:
		if word in freq_map.keys():
			features.append(freq_map[word])
		else:
			features.append(0)
	return np.array(features)

def create_training_matrices(left, right):
	"""
	Creates the feature data and result matrices to be trained on
	"""
	all_words = get_all_words(left + right)
	feature_list = []
	result_list = []

	for article in right:
		feature_row = create_article_vector(all_words, get_freq_map(article))
		feature_list.append([1] + feature_row)
		result_list.append(1)

	for article in left:
		feature_row = create_article_vector(all_words, get_freq_map(article))
		feature_list.append([1] + feature_row)
		result_list.append(-1)

	feature_matrix = np.array(feature_list)
	result_matrix = np.array(result_list)
	return feature_matrix, result_matrix


def create_prediction_matrix(all_words, new):
	"""
	Creates the feature data matrix for the new data to be predicted on
	"""
	feature_list = []
	for article in new:
		feature_row = create_article_vector(all_words, get_freq_map(article))
		feature_list.append([1] + feature_row)
	return np.array(feature_list)

def train_model(left,right):
	# Train Model
	feature_matrix, result_matrix = create_training_matrices(left, right)
	clf = linear_model.LinearRegression()
	clf.fit(feature_matrix, result_matrix)
	return (clf, left, right)


def predict(model, left, right, new):
	"""
	Estimate the slant of each article in new based on left and right training examples.
	"""
	# Predict on new data
	all_words = get_all_words(left + right)
	prediction_matrix = create_prediction_matrix(all_words, new)
	prediction_list = []
	for i in range(len(prediction_matrix)):
		row_to_predict = prediction_matrix[i]
		prediction = round(model.predict(row_to_predict) + 3.18, 2)
		prediction_list.append(prediction)

	return np.array(prediction_list)

def writeToPklz(outfilename, obj):
	"""
	Store an object as a file
	"""
	output = gzip.open(outfilename, 'wb')
	try:
		pickle.dump(obj, output, -1)
	finally:
		output.close()

def getObjFromPklz(infilename):
	"""
	get an object file
	"""
	f = gzip.open(infilename, 'rb')
	try:
	    return pickle.load(f)
	finally:
	    f.close()


right_articles = [convert_file_to_string('conservative.txt')]
left_articles = [convert_file_to_string('huffpotext1.txt')]
all_words = get_all_words(left_articles + right_articles)

# model = train_model(left_articles, right_articles)[0]
# writeToPklz('first_clf', model)
model = getObjFromPklz('first_clf')
print predict(model, left_articles, right_articles, ['religion', 'Gay rights', 'to', 'conservative'])




