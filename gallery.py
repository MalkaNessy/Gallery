from bottle import *

foto_list = [  {'small':'numbers-01.jpg','big':'numbers-01.jpg'}, {'small':'numbers-02.jpg','big':'numbers-02.jpg'}, {'small':'numbers-06.jpg','big':'numbers-6.jpg'} , {'small':'numbers-09.jpg','big':'numbers-09.jpg'}, {'small':'numbers-12.jpg','big':'numbers-12.jpg'}]


def page_template(body_html):
  return '''<!DOCTYPE html>
    <html>
     <head>
         %s
     </head>
     <body>
    %s
   </body>
   </html>''' % (head+header, body_html)



head = '''
 <meta charset "utf-8">
  <title>Tanya Kolesnikova | Photogallery</title>
  <link rel="stylesheet" href='/css/main.css'>
   '''


header = '''
     <header>
      <a href="index.html" id="logo">
        <h1>Photoes</h1>
        <h2>of Tanya Kolesnikova</h2>
      </a>
      
      <nav>
        <ul>
          <li><a href="/" class="selected">Portfolio</a> </li>
          <li><a href="about.html">About</a> </li>
          <li><a href="contact.html">Contact</a> </li>
        </ul>      
       </nav>
     </header> 
   '''
wrapper = '''
          <div id="wrapper">
      <section>   
        <ul id="gallery">
          <li>
            <a href="">
              <img src="img/numbers-01.jpg" alt="">
              <p>image 1</p>
            </a>  
          </li>
          <li>
            <a href="">
              <img src="img/numbers-02.jpg" alt="">
              <p>image 2</p>
            </a>  
          </li>
          <li>
            <a href="">
              <img src="img/numbers-06.jpg" alt="">
              <p>image 3</p>
            </a>  
          </li>
          <li>
            <a href="">
              <img src="img/numbers-09.jpg" alt="">
              <p>image 4</p>
            </a>  
          </li>
          <li>
            <a href="">
              <img src="img/numbers-12.jpg" alt="">
              <p>image 5</p>
            </a>  
          </li>
        
        
        </ul>
      </section>
      
      <footer> 
        
        <p>&copy; 2016 Tanya Kolesnikova </p>
      </footer>
    </div>  
    '''



@route('/')
def root_page():
  wrapper = ''
  for n in range (0, len(foto_list)):
     wrapper = wrapper+'''
    <li>
            <a href="/%d.html">
              <img src="/small/%d.jpg" alt="">
              <p>image %s</p>
            </a>  
          </li>'''  % (n, n,n+1)
  html= '''
          <div id="wrapper">
      <section>   
        <ul id="gallery">'''+wrapper+''' </ul>
      </section>
      
      <footer> 
        
        <p>&copy; 2016 Tanya Kolesnikova </p>
      </footer>
    </div>  '''  
   
  return page_template(html)

@route('/css/main.css') #подключает файл с оформлением
def get_css():
   return static_file("main.css", root="css")


@route('/small/<id>.jpg') # url маленькой картинки
def getsmallpict(id):
  id = int (id)
  d=foto_list[id]
  pathToFile=d['small']
  return static_file(pathToFile, root='img')

@route('/btn/close') # url картинки "закрыть"
def getclose():
  pathToFile='close-btn.jpg'
  return static_file(pathToFile, root='img')

@route('/btn/prev') # url картинки "предыдущая"
def getprev():
  pathToFile='prev-btn.jpg'
  return static_file(pathToFile, root='img')

@route('/btn/next') # url картинки "следующая"
def getnext():
  pathToFile='next-btn.jpg'
  return static_file(pathToFile, root='img')


@route('/<id>.html') # url страницы с большой картинкой и кнопками
def big_html(id):
  id = int(id)
  html= ''
  headhtml = head + header+ closebtn
  prevbtn = prevButton(id)
  nextbtn = nextButton(id)
  
  html=html+ '<div id="bigpage">' + prevbtn +  '<div class="big-picture"> <img src="/small/' +str(id) +  '.jpg">' +'<p>%s</p>' + '</div>' + nextbtn +'</body></html>'
    
  html= headhtml+(html)% ('image name and description')
  return html


closebtn = '''
    <div class="close">
        <a href="">
            <img src="/btn/close" alt="">
        </a>
    </div>
'''


def prevButton (id):
  if id==0:
    html= '''
	<div class="btn">
	    <a href="/">
		<img src="/btn/prev" alt="">
	    </a>
        </div> 			
    '''
    
  else:  
    id=int(id)-1
    id=str(id)
    html= '''
	<div class="btn">
	    <a href="/%s.html">
		<img src="/btn/prev" alt="">
	    </a>
        </div> 			
    ''' % (id)
  return html



def nextButton (id):
  if id==len(foto_list)-1:
    html= '''
	<div class="btn">
	    <a href="/">
		<img src="/btn/next" alt="">
	    </a>
        </div> 			
    '''
    
  else: 
    id=int(id)+1
    id=str(id)
    html = '''
      <div class="btn">
	  <a href="/%s.html">
	      <img src="/btn/next" alt="">
	  </a>
      </div> 			
      '''  % (id)
  return html




'''
@route('/')
def root():
  
  html = ''
  for n in range (0, len(foto_list)-1):
     html = html+'  <a href="/%d.html"> <img src="/small/%d.jpg" /> </a>   % (n, n)'
                                
  html = '<div style="%s"> %s</div>' % (stl, html)  
  return html


@route('/<id>.html') # url страницы с большой картинкой и кнопками
def big_html(id):
  id = int(id)
  html=''
  
  if id==0:              #(если картинка первая в списке)
    html=html+ '<div>  <a href ="/"><img src="/prev-but.jpg"></a> </div> </div>'
  else:
    html=html+ '<div>  <a href ="/' +str(id-1)+' " ><img src=”/prev-but.png"></a> </div> </div>'
  
  html=html+'<div> <img src="/small/' +str(id) +  '.jpg"> </div>' 

  if id==len(foto_list)-1:               #(если картинка последняя в списке)
    html=html+'<div> <a href =’/0.html’><img src="/next-but.jpg"></a> </div>  </div>'

  html= html+'<div>   <a href ="/"><img src="/close-but.jpg"></a> </div>'

  html= "<body>"+html+"</body>"
  return html


@route('<id>.jpg') # url большой картинки
def getbigpict(id):
id = int (id)
  d=foto_list[id]
  pathToFile=d['big']
  return static_file(pathToFile, root='images')
       



'''

run(host='localhost', port=8080)
