from bs4 import BeautifulSoup


def certifications_parser(source):
    try:
        soup_source = BeautifulSoup(source, 'lxml')
        certifications = []
        certifications_elements = soup_source.select(
            '#certifications-section>ul>li')
        for listitem in certifications_elements:
            certification = listitem.select(
                'div.pv-certifications__summary-info>h3')[0].text
            authority = listitem.select(
                'div.pv-certifications__summary-info>p>span:nth-of-type(2)')[0].text
            certifications.append(
                {'certification': certification, 'authority': authority})
    except Exception as e:
        print('Exception : ' + e)
    return certifications
