from bs4 import BeautifulSoup


def education_parser(source):
    try:
        soup_source = BeautifulSoup(source, 'lxml')
        education = []
        education_elements = soup_source.select(
            'div.pv-entity__degree-info')
        for div in education_elements:
            school = div.select('div>h3')[0].text
            degree = div.select(
                'div>p.pv-entity__secondary-title.pv-entity__degree-name>span.pv-entity__comma-item')[0].text
            field = div.select(
                'div>p.pv-entity__secondary-title.pv-entity__fos>span.pv-entity__comma-item')[0].text
            education.append(
                {'institution': school, 'degree': degree, 'fieldOfStudy': field})
    except Exception as e:
        print('Exception : ' + e)
    return education
