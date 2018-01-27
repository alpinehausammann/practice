
page =('<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://udacity.com">')

def link_parser(page):
    search_criteria = ['<a href=', '>']
    #Points set where program will look for link_parser
    start_link = str(page).find(str(search_criteria[0]))
    #first match for the start part of search
    end_link = str(page)[start_link: ].find(str(search_criteria[1]))
    #first match for second part of search
    link = str(page)[(start_link+len(search_criteria[0])+1):(start_link+end_link-1)]
    #information found between search criteria
    return link

print(link_parser(page))
