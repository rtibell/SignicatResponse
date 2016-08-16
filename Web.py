import web


urls = (
  '/', 'Index',
  '/foo', 'Foo'
)

render = web.template.render('templates', base='base')
app = web.application(urls, globals())
app.internalerror = web.debugerror
    
class Index:
    def GET(self):
        
        name = 'Rasmus' 
        name = None   
        return render.index(name)

class Foo:
    def GET(self):
        return "Hello, fool!!"


if __name__ == "__main__": 
    
    app.run()  