import web


urls = (
  '/', 'Index',
  '/callback', 'CallBack'
)

render = web.template.render('templates', base='base')
app = web.application(urls, globals())
app.internalerror = web.debugerror
    
class Index:
    def GET(self):
        
        name = 'Rasmus' 
        name = None   
        return render.index(name)

class CallBack:
    def GET(self):
        data = web.input()
        print("GET request to callback with param") 
        for i in data:
            print("{} = {}".format(i, [data[i]]))      
        return render.callback(len(data))


if __name__ == "__main__": 
    
    app.run()  