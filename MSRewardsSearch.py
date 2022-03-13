import webbrowser

url1 ='https://www.kozakdev.com/'
search_terms = ['dog','cat','kozakdev','quito','car','mountain','ocean','house','boat','phone','spotify','printer','mandiant','apple','pear','piano','coffee','quito','straw'
                'bank','school','duck','swan','glass','chocolate','pasta','cookie','F1','android','windows','headset','watch','maple','rewards','starbucks','truck','bing','weather',
                'art','paint','sun','cloud','keboard']
for term in search_terms:
    url = "https://www.bing.com/search?q={}".format(term) #more points on bing
    webbrowser.register('edge',
     None,
    webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")) #Rewards are only on Edge
    webbrowser.get('edge').open_new_tab(url)