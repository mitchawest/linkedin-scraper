from bs4 import BeautifulSoup


def skills_parser(source):
    try:
        soup_source = BeautifulSoup(source, 'lxml')
        skills = []
        top_skills_elements = soup_source.select(
            'ol.pv-skill-categories-section__top-skills>li')
        for listitem in top_skills_elements:
            skill = listitem.select(
                'span.pv-skill-category-entity__name-text')[0].text
            endorsements = listitem.select(
                'span.pv-skill-category-entity__endorsement-count')[0].text
            skills.append({'skill': skill.replace('\n', '').replace(
                '  ', ''), 'endorsementCount': endorsements})

        expanded_skills_elements = soup_source.select(
            'ol.pv-skill-category-list__skills_list>li')
        for listitem in expanded_skills_elements:
            skill = listitem.select(
                'span.pv-skill-category-entity__name-text')[0].text
            endorsements = listitem.select(
                'span.pv-skill-category-entity__endorsement-count')
            if not endorsements:
                endorsements = 0
            else:
                endorsements = endorsements[0].text
            skills.append({'skill': skill.replace('\n', '').replace(
                '  ', ''), 'endorsementCount': endorsements})
    except Exception as e:
        print('Exception : ' + e)
    return skills
