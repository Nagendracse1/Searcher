import bs4, requests


def google_play(package_name):

    res = requests.get(
        'https://play.google.com/store/apps/details?id=' + package_name, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
    try:
        res.raise_for_status()
    except:
        print('error------------')
        return {'Invalid_Package_name':"Invalid Package name"}

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    name = soup.select('h1 > span')
    if name == []:
        name = 'Not available'
    else:
        name = name[0].text

    icon = soup.select('div.hkhL9e > div > img')
    if icon == []:
        image_url = 'Not available'
    else:
        image_url = icon[0].get('src')

    developer = soup.select('span:nth-child(1) > a')
    if developer == []:
        developer = 'Not available'
    else:
        developer = developer[0].text

    description = soup.select('div.DWPxHb > span > div')
    if description == []:
        description = 'Not available'
    else:
        description = description[0].text[:200] + '...'

    no_downloads = soup.select('div:nth-child(3) > span > div > span')
    if no_downloads == []:
        no_downloads = 'Not available'
    else:
        no_downloads = no_downloads[0].text

    rating = soup.select(' div.jdjqLd > div.dNLKff > c-wiz > div > div')
    if rating == []:
        rating = 'Not available'
    else:
        rating = rating[0].get('aria-label')

    no_of_review = soup.select('c-wiz > div.K9wGie > span')
    if no_of_review == []:
        no_of_review = 'Not available'
    else:
        no_of_review = no_of_review[0].text

    print(name, image_url, developer, description, no_downloads, rating, no_of_review)
    return {
        'name':name,
        'image_url':image_url,
        'developer':developer,
        'description':description,
        'no_downloads':no_downloads,
        'rating':rating,
        'no_of_review':no_of_review
    }




def apple_store(name, application_id):
    name1 = ''
    for i in name:
        if i.isalnum() or i == ' ':
            if i == " ":
                name1 += '-'
            else:
                name1 += i

    res = requests.get(
        'https://apps.apple.com/in/app/' + name1 + '/id' + application_id, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
    try:
        res.raise_for_status()
    except:
        return {'Invalid_Package_name':"Invalid Package name"}

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    name = soup.select('header > h1')
    if name == []:
        name = 'Not available'
    else:
        name = name[0].text.strip()
        name1 = ''
        for i in name:
            if i == '\n':
                break
            name1 += i

    icon = soup.select(
        'img.we-artwork__image')
    if icon == []:
        image_url = 'Not available'
    else:
        image_url = icon[0].get('src')

    developer = soup.select(
        'h2.product-header__identity.app-header__identity > a')
    if developer == []:
        developer = 'Not available'
    else:
        developer = developer[0].text.strip()

    description = soup.select(
        'div.we-truncate')
    if description == []:
        description = 'Not available'
    else:
        description = description[0].text[:200] + '...'

    no_downloads = 'Not available'

    rating = soup.select('div.we-customer-ratings__averages > span')
    if rating == []:
        rating = 'Not available'
    else:
        rating = rating[0].text

    no_of_review = soup.select(
        'div.we-customer-ratings__count.small-hide.medium-show')
    if no_of_review == []:
        no_of_review = 'Not available'
    else:
        no_of_review = no_of_review[0].text
    #print(name1, image_url, developer, description,no_downloads, rating, no_of_review)
    return {
        'name':name1,
        'image_url':image_url,
        'developer':developer,
        'description':description,
        'no_downloads':no_downloads,
        'rating':rating,
        'no_of_review':no_of_review,
    }



#google_play(input())
#apple_store("The Love Boat - Puzzle Cruise ", "1477162888")


def key_find(url):

    print('Scrapping-------------Key')


    try:
        res = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
        res.raise_for_status()
    except:
        print('error------------Key')
        return 'Invalid URL'


    s = bs4.BeautifulSoup(res.text, 'html.parser')
    keyword_ele = s.select('head > meta')
    # print(keyword_ele)
    s = ''
    for i in range(len(keyword_ele)):
        # print(keyword_ele[i].get('name'))
        if keyword_ele[i].get('name') == "keywords":
            s += keyword_ele[i].get('content') + ','
        elif keyword_ele[i].get('name') == "description":
            s += keyword_ele[i].get('content') + ','
        elif keyword_ele[i].get('name') == "og:description":
            s += keyword_ele[i].get('content') + ','

    return s.rstrip(',')

