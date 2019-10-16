from bs4 import BeautifulSoup


def experience_parser(source):
    try:
        soup_source = BeautifulSoup(source, 'lxml')
        experience = []
        experience_elements = soup_source.select('#experience-section>ul>li')
        for listitem in experience_elements:
            sub_list_elements = listitem.select(
                'section.pv-profile-section__card-item-v2>ul>li')
            if len(sub_list_elements) == 0:
                company = listitem.select(
                    'div.pv-entity__summary-info>p.pv-entity__secondary-title')[0].text
                title = listitem.select(
                    'div.pv-entity__summary-info>h3')[0].text
                date_time_location = listitem.select('h4>span:nth-of-type(2)')
                responsibilities = []
                responsibilities_elements = listitem.select(
                    'div.pv-entity__extra-details>p>span')
                for responsibility in responsibilities_elements:
                    if 'SEE MORE' not in responsibility.text.upper():
                        responsibilities.append(
                            responsibility.text.replace('\n', '').replace('  ', ''))
                experience.append({'company': company, 'title': title,
                                   'dates': date_time_location[0].text, 'duration': date_time_location[1].text, 'location': date_time_location[2].text, 'responsibilities': responsibilities})
            else:
                company = listitem.select(
                    'div.pv-entity__company-summary-info>h3>span:nth-of-type(2)')[0].text
                for subitem in sub_list_elements:
                    title = subitem.select('h3>span:nth-of-type(2)')[0].text
                    date_time_location = subitem.select(
                        'h4>span:nth-of-type(2)')
                    responsibilities = []
                    responsibilities_elements = subitem.select(
                        'div.pv-entity__extra-details>p>span')
                    for responsibility in responsibilities_elements:
                        if 'SEE MORE' not in responsibility.text.upper():
                            responsibilities.append(
                                responsibility.text.replace('\n', '').replace('  ', ''))
                    experience.append({'company': company, 'title': title, 'dates': date_time_location[0].text, 'duration': date_time_location[
                        1].text, 'location': date_time_location[2].text, 'responsibilities': responsibilities})
    except Exception as e:
        print('Exception : ' + e)
    return experience
