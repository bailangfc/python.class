#1.想使用父类中的方法的两种方式
#super函数和父类.函数

class Person(object):
    def __init__(self,web_site):
        self.web=web_site

    def update_web(self,site):
        self.web=site
        return self.web
class LaoQi(Person):
    def __init__(self,teacher,web_site):
        self.teacher=teacher
        # Person.__init__(self,web_site)
        super(LaoQi,self).__init__(web_site)
        
    def update_web(self,site,lang="python"):
        self.web=site
        self.lang=lang
        return  self.web,self.lang
    def your_teacher(self):
        return self.teacher

    def about_me(self,name,site):
        my_web,my_lang=self.update_web(site)
        return {"name":name,"web":my_web,"lang":my_lang}

if __name__=="__main__":
    #my=Person("www.qq.com")
    my=LaoQi("bailang","www.qq.com")
    print my.your_teacher()
    print my.teacher
    print my.web
    
#多重继承
class Person(object):
    def eye(self):
        print "two eyes"

    def breast(self,n):
        print "The breast is:",n

class Girl(object):
    def __init__(self,age):
        self.age=age

    def color(self):
        print "The girl is white."

class BeaGirl(Person,Girl):
    pass

if __name__=="__main__":
    kong=BeaGirl(28)
    kong.eye()
    kong.breast(90)
    kong.color()
    print kong.age
    
#多重继承  
#广度优先继承
class K1(object):
    def foo(self):
        print "K1-foo"

class K2(object):
    def foo(self):
        print "K2-foo"
    def bar(self):
        print "K2-bar"

class J1(K1,K2):
    pass

class J2(K1,K2):
    def bar(self):
        print "J2-bar"

class C(J1,J2):
    pass

if __name__=="__main__":
    print C.__mro__   #打印C的继承顺序
    m=C()
    m.foo()
    m.bar()
