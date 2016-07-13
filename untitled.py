img_list = [{'small':'numbers-01.jpg'}, {'small':'numbers-02.jpg'} ]




TODO
== чтобы с первой картинки назад попадать на главную страницу
== чтобы с последней картинки вперед попадать на главную страницу
== чтобы со слова "портфолио" попадать на главную страницу
== создать функцию для описания картинки




def prevButton (id):
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

def big_html(id):
  id = int(id)
  html= ''
  
  theprevbtn=prevbtn(id)

  html=html+ '<div id="bigpage">' + theprevbtn +  '<div class="big-picture"> <img src="/small/' +str(id) +  '.jpg">' +'<p>%s</p>' + '</div>' +'</body></html>'
    
    
  html= (html)% ('image name and description')
  return html

print (prevButton(3))
