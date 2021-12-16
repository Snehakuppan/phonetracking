
sneha={"instagram":{"photos":90,"gb used":"100mb","time consumed":"1 hr"},
       "watsapp":{"photos":50,"gb used":"500mb","time consumed":"5 hr"},
       "snapchat":{"photos":40,"gb used":"800mb","time consumed":"3 hr"}}
class tracking:
    def __init__(self,app):
        self.app=app
    def gpused(self):
        for k,v in sneha[self.app].items():
            if k =="gb used":
                if v >"500mb":
                    print("over used more than 500mb:",v)
                else:
                    print("databuse:",v,end="")
        show()
    def hourconsumed(self):
        for k,v in sneha[self.app].items():
            if k =="time consumed":
                if v >"1hr":
                    print("over used more than 1hr:",v)
                else:
                    print("time consumed:",v,end="")
        show()     
    def photohub(self):
        for k,v in sneha[self.app].items():
            if k =="photos":
                if v >"50":
                    print("more than 50:",v)
                else:
                    print("less than 50:",v,end="")
        show()     
                    
        
        
                    
def show():
    print("1.to check gp used",
          "2.to check for time consumed",
          "3.to check how photos stored")
    
    choose=int(input("choose any one "))
    
    if choose==1:
        app1=input("enter app to check gp used:")
    
        res=tracking(app1)
        res.gpused()
    elif choose==2:
        app2=input("enter app to check time consumed:")
        ret=tracking(app2)
        ret.hourconsumed()
    elif choose==3:
        
        app3=input("enter app to check photos in app")
        rev=tracking()
        rev.photohub()
        
        
show()    
            
