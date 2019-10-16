from bs4 import BeautifulSoup
import os


def recommendations_parser(source):
    try:
        soup_source = BeautifulSoup(source, 'lxml')
        recommendations = []
        recommendations_elements = soup_source.select(
            'ul.section-info>li.pv-recommendation-entity')
        for listitem in recommendations_elements:
            recommendor = listitem.select(
                'div.pv-recommendation-entity__detail>h3')[0].text
            recommendor_title = listitem.select(
                'div.pv-recommendation-entity__detail>p.pv-recommendation-entity__headline')[0].text
            recommendation = listitem.select(
                'span.lt-line-clamp__raw-line')[0].text
            if os.environ['LI_RECOMMENDEE_NAME'] in recommendation.upper():
                recommendations.append(
                    {'recommendor': recommendor, 'title': recommendor_title, 'recommendation': recommendation})
    except Exception as e:
        print('Exception : ' + e)
    return recommendations
