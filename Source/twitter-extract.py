next_index = 0 # the next page position from which the URL search starts

def get_net_target(page):
  global next_index

  #start_link=page.find("href=" or "http:" or "https:")
  start_link=page.find("https")
  if start_link == -1: # no more URL
    return ""
  
  start_quote=page.find(' https',start_link)
  end_quote=page.find("'",start_quote+1)
#  end_quote1=page.find(" ",start_quote+1)
  next_index=end_quote
  url=page[start_quote+1:end_quote]
  end_quote=5
  return url


my_file = open("twit_data_out.txt")
page = my_file.read()

while True:
    url = get_net_target(page)
    if url == "": # no more URL
        break
    print(url[0:26])
    page = page[next_index:] # continue with the page

