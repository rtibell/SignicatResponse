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
        inp = web.input(name=None)
        print("GET request to callback with param {}".format(inp.name))      
        return render.callback(inp.name)


if __name__ == "__main__": 
    
    app.run()  